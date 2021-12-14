from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Product(models.Model):
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,default="")
    count = models.IntegerField(default=0)
    detail = models.CharField(max_length=999,default="")    
    def __str__(self):
        return "Name "+str(self.name)+ "|Price "+str(self.price)+"|Count "+ str(self.count)

class Storage(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name
