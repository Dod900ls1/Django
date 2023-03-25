from django.db import models


class Director(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    portraint = models.ImageField(upload_to='portraints/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first} {self.last}"
