# Generated by Django 3.2.6 on 2021-08-28 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210821_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopp',
            name='active',
        ),
        migrations.RemoveField(
            model_name='shopp',
            name='thumb',
        ),
    ]
