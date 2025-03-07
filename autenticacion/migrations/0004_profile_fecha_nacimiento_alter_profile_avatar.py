# Generated by Django 5.1.6 on 2025-03-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("autenticacion", "0003_alter_profile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="fecha_nacimiento",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="avatars/default.jpg", upload_to="avatars/"
            ),
        ),
    ]
