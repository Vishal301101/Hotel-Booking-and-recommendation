# Generated by Django 4.2.7 on 2023-11-21 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_remove_userprofile_profile_picture_userprofile_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='image_path',
        ),
    ]