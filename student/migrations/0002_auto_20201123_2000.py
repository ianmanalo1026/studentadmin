# Generated by Django 3.1.1 on 2020-11-23 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='student',
            new_name='user',
        ),
    ]
