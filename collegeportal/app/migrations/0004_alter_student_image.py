# Generated by Django 5.1.1 on 2024-09-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
