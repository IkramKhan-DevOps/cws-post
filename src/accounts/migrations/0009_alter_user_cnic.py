# Generated by Django 3.2.9 on 2022-02-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_cnic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cnic',
            field=models.CharField(help_text='13 digits cnic without -', max_length=13),
        ),
    ]
