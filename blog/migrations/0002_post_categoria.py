# Generated by Django 5.1 on 2024-08-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('tech', 'Technology'), ('lifestyle', 'Lifestyle'), ('education', 'Education'), ('news', 'News')], default='tech', max_length=30),
        ),
    ]