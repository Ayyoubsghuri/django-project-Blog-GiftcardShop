# Generated by Django 3.2.6 on 2021-08-21 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_shoporder_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoporder',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AlterModelOptions(
            name='shopp',
            options={'ordering': ['-updated_on']},
        ),
    ]
