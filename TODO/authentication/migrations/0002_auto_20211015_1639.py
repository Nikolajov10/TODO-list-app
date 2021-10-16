# Generated by Django 3.2.8 on 2021-10-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regusers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='regusers',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
