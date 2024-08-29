# Generated by Django 5.1 on 2024-08-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen_banner', models.ImageField(blank=True, null=True, upload_to='banners/', verbose_name='Imagen de Banner')),
                ('contenido_embebido', models.TextField(blank=True, null=True, verbose_name='Contenido Embebido (HTML)')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Última Actualización')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
