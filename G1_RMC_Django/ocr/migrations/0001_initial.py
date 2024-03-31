# Generated by Django 5.0.3 on 2024-03-26 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.FloatField()),
                ('unit_price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('client_name', models.CharField(max_length=200)),
                ('billing', models.CharField(max_length=200)),
                ('delivery', models.CharField(max_length=200)),
                ('invoice_no', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('items', models.ManyToManyField(to='ocr.item')),
            ],
        ),
        migrations.CreateModel(
            name='OCRResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ocr_images/')),
                ('extracted_text', models.TextField()),
                ('data', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocr.invoice')),
            ],
        ),
    ]
