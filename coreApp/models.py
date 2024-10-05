from django.db import models


class Visitors(models.Model):

    title = models.CharField(max_length=200, default='tit;e')
    text = models.CharField(max_length=2000, default='text')
    ipaddress = models.GenericIPAddressField()
    date = models.DateTimeField()
    language = models.CharField(max_length=200, default='language')
    accent = models.CharField(max_length=200, default='accesnt')

    def __str____(self):
        return f'{self.title} , {self.text}'

# Create your models here.
