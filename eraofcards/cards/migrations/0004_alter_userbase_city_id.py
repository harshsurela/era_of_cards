# Generated by Django 3.2.9 on 2022-08-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20220824_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.city'),
        ),
    ]
