# Generated by Django 3.0.1 on 2020-08-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immm',
            name='image',
            field=models.ImageField(upload_to='staticfiles/'),
        ),
    ]
