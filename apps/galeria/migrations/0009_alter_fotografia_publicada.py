# Generated by Django 4.1.7 on 2023-03-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
