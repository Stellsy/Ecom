# Generated by Django 2.2.14 on 2020-11-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201115_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]