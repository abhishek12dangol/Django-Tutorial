from django.db import models

# Create your models here
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Test(models.Model):
    name = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return f"Student {self.name}"