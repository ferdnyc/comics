# Generated by Django 4.2.1 on 2023-05-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0059_comic_secret_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='cloudflare_token',
            field=models.CharField(blank=True, help_text='Your Cloudflare API Token', max_length=50),
        ),
        migrations.AddField(
            model_name='comic',
            name='cloudflare_zone',
            field=models.CharField(blank=True, help_text='Your Cloudflare Zone ID', max_length=50),
        ),
    ]
