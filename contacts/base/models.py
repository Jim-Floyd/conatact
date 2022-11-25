from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=20)
    number = models.CharField(max_length=9)

    def __str__(self) -> str:
        return str(self.username)
