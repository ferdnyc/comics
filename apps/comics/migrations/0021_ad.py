# Generated by Django 2.1.5 on 2019-01-27 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0020_tagtype_default_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ads', to='comics.Comic')),
            ],
        ),
    ]
