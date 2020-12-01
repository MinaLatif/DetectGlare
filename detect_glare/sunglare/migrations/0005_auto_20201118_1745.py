# Generated by Django 3.1.3 on 2020-11-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunglare', '0004_remove_post_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='epoch',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='orientation',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
