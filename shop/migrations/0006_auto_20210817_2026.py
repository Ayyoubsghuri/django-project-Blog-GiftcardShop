# Generated by Django 3.2.6 on 2021-08-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210817_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopp',
            name='acclst',
        ),
        migrations.RemoveField(
            model_name='shopp',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='shoporder',
            name='user',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
