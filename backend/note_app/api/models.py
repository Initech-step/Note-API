from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.category)


class Notes(models.Model):
    note = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.note)