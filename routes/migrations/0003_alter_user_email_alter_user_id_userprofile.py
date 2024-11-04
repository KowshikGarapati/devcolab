# Generated by Django 5.0.2 on 2024-10-01 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=200)),
                ('github_url', models.URLField(unique=True)),
                ('linkedin_url', models.URLField(unique=True)),
                ('followers', models.ManyToManyField(related_name='followers', to='routes.userprofile')),
                ('following', models.ManyToManyField(related_name='following', to='routes.userprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='routes.user')),
            ],
        ),
    ]