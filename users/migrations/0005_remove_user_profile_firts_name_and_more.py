# Generated by Django 4.0.4 on 2022-06-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_profile_descripcion_user_profile_firts_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='firts_name',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='last_name',
        ),
    ]
