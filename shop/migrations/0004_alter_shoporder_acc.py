# Generated by Django 3.2.6 on 2021-08-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shoporder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoporder',
            name='acc',
            field=models.CharField(max_length=200),
        ),
    ]
