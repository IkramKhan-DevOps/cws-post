# Generated by Django 3.2.12 on 2022-03-19 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_parcel_postman'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='status',
            field=models.CharField(default='ssm', max_length=3),
        ),
    ]
