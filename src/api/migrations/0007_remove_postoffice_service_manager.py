# Generated by Django 3.2.12 on 2022-03-16 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220316_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postoffice',
            name='service_manager',
        ),
    ]
