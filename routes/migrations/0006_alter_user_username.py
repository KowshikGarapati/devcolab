# Generated by Django 5.0.2 on 2024-10-21 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]