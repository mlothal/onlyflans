# Generated by Django 4.2 on 2024-06-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_flan_precio_alter_flan_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
