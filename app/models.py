from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=60)
    pseudonym = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    mail = models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.pseudonym


class Ticket(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)


class Concert(models.Model):
    name = models.CharField(max_length=30)
    ticket = models.ManyToManyField(Ticket)
    musician = models.ManyToManyField(Musician)
    date = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)


class User(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)


class Order(models.Model):
    number = models.IntegerField()
    amount = models.IntegerField()
    ticket = models.ManyToManyField(Ticket)
    user = models.ManyToManyField(User)


class CustomUser(models.Model):
    username = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
