# Generated by Django 3.1 on 2025-03-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_variation'),
        ('carts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store_app.Variation'),
        ),
    ]
