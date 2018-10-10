# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-04 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0043_remove_ods_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='initiatives',
            field=models.ManyToManyField(related_name='_initiative_initiatives_+', to='models.Initiative', verbose_name='Relaciones'),
        ),
    ]
