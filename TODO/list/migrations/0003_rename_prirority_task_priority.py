# Generated by Django 3.2.8 on 2021-10-16 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_task_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='prirority',
            new_name='priority',
        ),
    ]
