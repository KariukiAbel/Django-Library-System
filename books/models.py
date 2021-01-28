from django.db import models

# Create your models here.

#creates a table in db.sqlite
class Book(models.Model):
    
    #returns the database results
    def __str__(self):
        return self.name + " - " + self.author
    
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    
#syntax for creating a table 
# class table_name(models.Model):
#     attributes come here
