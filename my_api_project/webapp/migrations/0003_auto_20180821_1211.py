# Generated by Django 2.1 on 2018-08-21 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180821_1201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='People',
            new_name='Person',
        ),
    ]