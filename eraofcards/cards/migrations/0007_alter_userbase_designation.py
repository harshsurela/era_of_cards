# Generated by Django 3.2.9 on 2022-08-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_package_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='designation',
            field=models.CharField(blank=True, default='Not Given', max_length=255, null=True),
        ),
    ]