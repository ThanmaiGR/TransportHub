# Generated by Django 5.0.2 on 2024-02-14 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cabfarestructure_companyid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stops',
            old_name='Location',
            new_name='LocationID',
        ),
    ]
