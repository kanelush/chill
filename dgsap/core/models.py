from django.db import models
import datetime
import random
# Create your models here.


def random_string():
      return str(random.randint(1000000, 99999999))

class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.IntegerField()
   description = models.TextField()
   buy_order = models.CharField(default=random_string, max_length=100)
   session_id = models.CharField(default=random_string, max_length=100)

   def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    created = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)
    fieldo = models.CharField(max_length=20, blank=True)
    mail = models.EmailField(max_length=254, blank=True)
   

    def __str__(self):
        return self.subject


