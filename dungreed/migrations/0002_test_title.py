# Generated by Django 2.2.3 on 2019-09-19 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dungreed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
