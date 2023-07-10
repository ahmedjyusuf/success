# Generated by Django 4.1.3 on 2023-07-10 05:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zoom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zoomclassschedule',
            name='student',
        ),
        migrations.AddField(
            model_name='zoomclassschedule',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
