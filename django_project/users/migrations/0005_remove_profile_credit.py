# Generated by Django 3.2.8 on 2022-07-12 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='credit',
        ),
    ]
