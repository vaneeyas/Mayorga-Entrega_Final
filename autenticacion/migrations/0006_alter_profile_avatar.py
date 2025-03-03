# Generated by Django 5.1.6 on 2025-03-03 01:14

import autenticacion.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("autenticacion", "0005_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="avatars/default.JPG",
                null=True,
                upload_to=autenticacion.models.avatar_upload_path,
            ),
        ),
    ]
