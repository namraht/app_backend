from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Expertise(models.Model):
    work_category=models.CharField(max_length=50)


class Rating(models.Model):
    #repairer_id=models.IntegerField()
    rating=models.DecimalField(decimal_places=4,max_digits=12)
    reviews=models.CharField(max_length=200)


class Repairer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cnic=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=20)
    #location=models.CharField(max_length=200)      ***
    password=models.CharField(max_length=20)
    secret_question=models.CharField(max_length=200)
    secret_answer=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    expertise = models.ManyToManyField('Expertise')
    rating = models.ForeignKey('Rating')


class Shop(models.Model):
    shop_name=models.CharField(max_length=50)
    #shop_location=models.CharField(max_length=12)  ***
    repairer_id=models.ForeignKey('Repairer')
   # pk


class Favourites(models.Model):
    repairer_id=models.IntegerField()

class Userr(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cnic=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=20)
    #location=models.CharField(max_length=200)
    password=models.CharField(max_length=20)
    secret_question=models.CharField(max_length=200)
    secret_answer=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    fav=models.ForeignKey('Favourites')
    rating = models.ForeignKey('Rating')

