# Generated by Django 5.0.3 on 2024-03-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.FloatField()),
                ('unit_price', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
            ],
        ),
    ]