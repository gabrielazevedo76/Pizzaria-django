from email.policy import default
from django.db import models
from secrets import choice

# Create your models here.

class Order(models.Model):

    PIZZA_SIZE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    SITUATION = {
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    }

    name = models.CharField(max_length=45)
    email = models.CharField(max_length=50)
    size = models.CharField(max_length=30, choices=PIZZA_SIZE)
    flavour = models.ForeignKey('Flavor', on_delete=models.CASCADE) 
    obs_message = models.CharField(max_length=300, null=True)
    situation = models.CharField(max_length=30, null=True, choices=SITUATION, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Flavor(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.CharField(max_length=300)
    cover = models.ImageField(
        upload_to='App/media/img/%Y/%m/%d/', blank=True, default=''
    )

    def __str__(self):
        return self.name
