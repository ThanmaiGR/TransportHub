# Generated by Django 5.0.2 on 2024-03-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_routedetails_arrivaltime_delete_schedules'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabfarestructure',
            name='BaseKM',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=4),
            preserve_default=False,
        ),
    ]
