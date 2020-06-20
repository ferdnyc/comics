# Generated by Django 3.0.7 on 2020-06-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0037_auto_20200620_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkedsocialplatform',
            name='call_to_action',
            field=models.CharField(blank=True, help_text='If not blank, overrides the platform CTA.', max_length=128),
        ),
        migrations.AddField(
            model_name='linkedsocialplatform',
            name='title',
            field=models.CharField(blank=True, help_text='If not blank, overrides the platform name.', max_length=64),
        ),
        migrations.AddField(
            model_name='socialplatform',
            name='call_to_action',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
