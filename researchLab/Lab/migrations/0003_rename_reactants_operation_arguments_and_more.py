# Generated by Django 4.1.1 on 2023-03-07 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0002_operation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='reactants',
            new_name='arguments',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='pick_beaker',
        ),
    ]
