# Generated by Django 2.0.7 on 2018-09-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_geo_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
