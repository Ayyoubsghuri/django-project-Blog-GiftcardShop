# Generated by Django 3.2.6 on 2021-08-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userpass_ipcountry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpass',
            name='ip',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
    ]
