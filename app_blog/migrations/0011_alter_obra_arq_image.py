# Generated by Django 4.0.4 on 2022-06-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0010_arquitecto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra_arq',
            name='image',
            field=models.ImageField(default='default', upload_to='obras'),
        ),
    ]
