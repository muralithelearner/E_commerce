# Generated by Django 4.2 on 2023-11-12 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_registrationpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationpage',
            old_name='mobile_or_email',
            new_name='contactinput',
        ),
    ]