# Generated by Django 2.0.7 on 2018-09-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_profile_zoom'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='select',
            field=models.CharField(blank=True, max_length=200, verbose_name='Select'),
        ),
        migrations.AddField(
            model_name='profile',
            name='zoom',
            field=models.CharField(blank=True, max_length=2, verbose_name='Zoom'),
        ),
    ]
