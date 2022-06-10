# Generated by Django 4.0.5 on 2022-06-10 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import occasion_bot.consts


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram', '0003_telegramchannel_from_region_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=3800, null=True)),
                ('expected_date', models.DateField()),
                ('status', enumfields.fields.EnumField(default='active', enum=occasion_bot.consts.IssueStatus, max_length=16)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='telegram.telegramchannel')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issues_created', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues_executed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='occasion_bot.issue')),
            ],
        ),
    ]
