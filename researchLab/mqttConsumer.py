# python3.6

import random

from paho.mqtt import client as mqtt_client
import queue


#from .views import addInd


import psycopg2

#establishing the connection
conn = conn = psycopg2.connect(
   database="admin", user='root', password='root', host='db', port= '5432'
)


cur=conn.cursor()
try:
    cur.execute("CREATE TABLE testBeaker(id SERIAL PRIMARY KEY,beakerId VARCHAR);")
    conn.commit()
    print("Beaker table created")
except:
    conn.rollback()
    print("Beaker table already created")


try:
    cur.execute("CREATE TABLE testSlot(id SERIAL PRIMARY KEY,slotId VARCHAR);")
    conn.commit()
    print("slot table created")
except:
    conn.rollback()
    print("Slot table already created")

try:
    cur.execute("CREATE TABLE testComment(id SERIAL PRIMARY KEY,comment VARCHAR);")
    conn.commit()
    print("comment table created")
except:
    conn.rollback()
    print("comment table already created")


q=queue.Queue(maxsize=6)
broker = 'broker.mqttdashboard.com'
port = 1883
topic = [("dropDown/slot", 0), ("dropDown/Beaker", 0),("comment",0)]
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        str1=msg.payload.decode()
        print(f"Received `{str1}` from `{msg.topic}` topic\n")
        # x=str.split(",")
        # print(x)
        # s,q,p=[],[],[]
        # s=x[0].split()
        # q=x[1].split()
        # p=x[2].split()
        #file = open('beaker.txt','w')
        #file.write(str1)
        #file.close()
        if msg.topic == "dropDown/Beaker":
            cur.execute('INSERT INTO testBeaker (beakerId) VALUES(%s)',(str1,))
            conn.commit()
        
        if msg.topic == "dropDown/slot":
            cur.execute('INSERT INTO testSlot (slotId) VALUES(%s)',(str1,))
            conn.commit()
        
        if msg.topic == "comment":
            cur.execute('INSERT INTO testComment (comment) VALUES(%s)',(str1,))
            conn.commit()


        q.put(str)


    
        

        

    client.subscribe(topic, 0)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   run()