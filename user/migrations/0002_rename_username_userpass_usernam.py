# Generated by Django 3.2.6 on 2021-08-28 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpass',
            old_name='username',
            new_name='usernam',
        ),
    ]
