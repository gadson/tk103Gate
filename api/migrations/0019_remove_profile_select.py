# Generated by Django 2.0.7 on 2018-09-15 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20180915_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='select',
        ),
    ]
