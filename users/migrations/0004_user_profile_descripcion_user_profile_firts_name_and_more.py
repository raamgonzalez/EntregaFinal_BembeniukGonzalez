# Generated by Django 4.0.4 on 2022-06-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='descripcion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='firts_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='last_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
