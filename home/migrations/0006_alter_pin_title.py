# Generated by Django 4.2.4 on 2023-11-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_pin_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]