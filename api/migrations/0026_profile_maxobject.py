# Generated by Django 2.0.7 on 2019-05-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190316_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='maxobject',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
