# Generated by Django 3.2.6 on 2021-08-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210828_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpass',
            name='ipCountry',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
