from django.db import models

class Contacts(models.Model):
    username=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.username



