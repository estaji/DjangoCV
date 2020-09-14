# Generated by Django 2.2.6 on 2020-09-14 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_bar'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='github',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bar',
            name='linkedin',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]