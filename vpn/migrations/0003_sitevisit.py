# Generated by Django 4.2.15 on 2024-08-27 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vpn', '0002_usersite'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data_sent', models.PositiveIntegerField(default=0)),
                ('data_received', models.PositiveIntegerField(default=0)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vpn.usersite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
