# Generated by Django 3.2.12 on 2022-03-19 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_alter_parcel_destination_service_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='postman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postman', to=settings.AUTH_USER_MODEL),
        ),
    ]
