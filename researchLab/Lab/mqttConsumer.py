# python3.6

import random

from paho.mqtt import client as mqtt_client
import queue


#from .views import addInd


import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='root', password='root', host='127.0.0.1', port= '5432'
)



cur=conn.cursor()

#cur.execute("CREATE TABLE testBeaker(id SERIAL PRIMARY KEY,beakerId VARCHAR);")

cur.execute("SELECT * FROM testBeaker")
print(cur.fetchall())

#conn.commit()






q=queue.Queue(maxsize=6)




broker = 'broker.mqttdashboard.com'
port = 1883
topic = "dropDown"
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
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic\n")
        str1=msg.payload.decode()
        # x=str.split(",")
        
        # print(x)
        # s,q,p=[],[],[]
        # s=x[0].split()
        # q=x[1].split()
        # p=x[2].split()

        print(str1)

        #file = open('beaker.txt','w')
        #file.write(str1)
        #file.close()

        cur.execute('INSERT INTO testBeaker (beakerId) VALUES(%s)',(str1,))

        conn.commit()

        q.put(str)


    
        

        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   run()