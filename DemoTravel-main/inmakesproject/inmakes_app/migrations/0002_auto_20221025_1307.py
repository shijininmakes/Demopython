# Generated by Django 3.0 on 2022-10-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmakes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]