from django.db import models

# Create your models here.


class Receipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    ingredients = models.TextField()
    directions = models.TextField()
    time = models.IntegerField()
    servings = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
    