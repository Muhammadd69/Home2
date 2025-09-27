from django.db import models


class Home(models.Model):
    image = models.ImageField(upload_to='images/home')
    type = models.CharField(max_length=120)
    price = models.IntegerField()
    city = models.TextField(null=True, blank=True)
    location = models.TextField()
    beds = models.TextField(null=True, blank=True)
    baths = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.city


class Customer(models.Model):
    image = models.ImageField(upload_to='images/customer')
    rating = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=120)
    descriptions = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Agent(models.Model):
    image = models.ImageField(upload_to='images/agent')
    name = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    descriptions = models.TextField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    def __str__ (self):
        return self.name