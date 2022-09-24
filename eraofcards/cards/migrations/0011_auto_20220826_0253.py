# Generated by Django 3.2.9 on 2022-08-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20220826_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='aboutme',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='bank_details',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='cus_add1',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='cus_add2',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='cus_phone',
            field=models.CharField(blank=True, default=' ', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='designation',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='fb',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='gps',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='ig',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='linkedin',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='organization',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='pincode',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='skype',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='twitter',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='visitor_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='website',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='yt',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
    ]
