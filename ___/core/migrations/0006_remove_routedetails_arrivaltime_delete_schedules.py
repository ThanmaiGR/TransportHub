# Generated by Django 5.0.2 on 2024-03-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_locations_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routedetails',
            name='ArrivalTime',
        ),
        migrations.DeleteModel(
            name='Schedules',
        ),
    ]
