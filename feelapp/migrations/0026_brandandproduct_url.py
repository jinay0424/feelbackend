# Generated by Django 5.0.7 on 2024-08-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feelapp", "0025_galleryimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="brandandproduct",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
