# Generated by Django 3.2.23 on 2024-01-29 10:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0008_messages'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='messages',
            unique_together={('user', 'from_user')},
        ),
    ]
