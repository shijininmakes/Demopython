# Generated by Django 4.2.4 on 2023-08-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='20-05-2001'),
            preserve_default=False,
        ),
    ]
