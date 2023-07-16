from django.db import models
class Contact(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=30)
   query = models.TextField(max_length=50)

