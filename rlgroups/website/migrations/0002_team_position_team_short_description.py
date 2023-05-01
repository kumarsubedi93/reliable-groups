# Generated by Django 4.2 on 2023-05-01 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]