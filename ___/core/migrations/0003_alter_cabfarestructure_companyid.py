# Generated by Django 5.0.2 on 2024-02-14 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_connections_destinationid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabfarestructure',
            name='CompanyID',
            field=models.OneToOneField(db_column='CompanyID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.cabcompanies'),
        ),
    ]
