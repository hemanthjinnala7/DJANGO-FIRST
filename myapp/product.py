from .category import Category
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='img')
    desc = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.category})" 

    
