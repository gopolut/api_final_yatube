# Generated by Django 2.2.16 on 2021-12-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211219_0154'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='uniq_following'),
        ),
    ]
