# Generated by Django 2.0 on 2018-02-08 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chioce',
            new_name='Choice',
        ),
    ]
