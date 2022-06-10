# Generated by Django 4.0.5 on 2022-06-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=62, unique=True),
        ),
    ]