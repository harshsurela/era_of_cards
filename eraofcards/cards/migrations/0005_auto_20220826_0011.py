# Generated by Django 3.2.9 on 2022-08-25 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_userbase_city_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='features',
            field=models.JSONField(default="{'demo':demo'}"),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]