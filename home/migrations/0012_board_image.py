# Generated by Django 4.2.4 on 2023-11-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='board'),
        ),
    ]