# Generated by Django 2.0.7 on 2019-03-16 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_push_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='push_id',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Profile'),
        ),
    ]
