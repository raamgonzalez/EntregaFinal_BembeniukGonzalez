# Generated by Django 4.0.4 on 2022-06-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0009_arquitecto_image_obra_arq_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquitecto',
            name='descripcion',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
