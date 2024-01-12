from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    
    def __str__(self):
        # return self.name + ': ' + self.description
        return f"{self.name}: {self.description}   Price: {self.price:.2f}"

class Sample(models.Model):
    name = models.CharField(max_length=100)