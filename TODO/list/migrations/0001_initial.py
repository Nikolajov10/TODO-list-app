# Generated by Django 3.2.8 on 2021-10-16 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=20000)),
                ('due_date', models.DateField()),
                ('prirority', models.CharField(max_length=10)),
            ],
        ),
    ]
