# Generated by Django 3.2.9 on 2022-09-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_auto_20220831_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='gps',
            field=models.URLField(blank=True, default=' ', max_length=500, null=True),
        ),
    ]