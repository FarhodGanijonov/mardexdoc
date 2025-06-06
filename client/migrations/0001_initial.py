# Generated by Django 5.1.6 on 2025-04-19 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='client/news_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientReyting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_orders', models.PositiveIntegerField(default=0)),
                ('completed_orders', models.PositiveIntegerField(default=0)),
                ('cancelled_orders', models.PositiveIntegerField(default=0)),
                ('reyting', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.CreateModel(
            name='ClientTarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('top_limit', models.PositiveIntegerField(default=2)),
                ('call_limit', models.PositiveIntegerField(default=3)),
            ],
            options={
                'verbose_name': 'Client Tarif',
                'verbose_name_plural': 'Client Tariflar',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, default='', null=True)),
                ('desc_ru', models.TextField(blank=True, default='', null=True)),
                ('desc_uz', models.TextField(blank=True, default='', null=True)),
                ('desc_en', models.TextField(blank=True, default='', null=True)),
                ('full_desc', models.TextField(blank=True, default='', null=True)),
                ('full_desc_ru', models.TextField(blank=True, default='', null=True)),
                ('full_desc_uz', models.TextField(blank=True, default='', null=True)),
                ('full_desc_en', models.TextField(blank=True, default='', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='client_image/')),
                ('worker_count', models.IntegerField(default=1)),
                ('client_is_finished', models.BooleanField(default=False)),
                ('worker_is_finished', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('Male', 'Erkak'), ('Female', 'Ayol')], default='Male', max_length=10)),
                ('view_count', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('stable', 'Stable'), ('success', 'Success'), ('in_progress', 'In_progress'), ('cancel_client', 'Cancel by Client'), ('cancel_worker', 'Cancel by Worker')], default='stable', max_length=20)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifHaridi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
