# Generated by Django 4.2.3 on 2023-07-25 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField(verbose_name='Inhalt')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Veröffentlicht')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Erstellt')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Geändert')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2, verbose_name='Status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blöcke',
            },
        ),
    ]
