# Generated by Django 4.2.4 on 2023-08-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='aaas', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
