from django.db import models

class residents(models.Model):
    username = models.CharField(max_length=150)
    Mobile_Phone = models.CharField(max_length=128)  # You should hash passwords for security

    def __str__(self):
        return self.username
