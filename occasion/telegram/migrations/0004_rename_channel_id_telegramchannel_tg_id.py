# Generated by Django 4.0.5 on 2022-06-10 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0003_telegramchannel_from_region_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramchannel',
            old_name='channel_id',
            new_name='tg_id',
        ),
    ]
