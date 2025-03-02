from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
