# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_initiative_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='image',
            field=models.ImageField(blank=True, help_text='Sube una imagen representativa de la iniciativa', upload_to='images/initiatives/', verbose_name='Imagen'),
        ),
    ]
