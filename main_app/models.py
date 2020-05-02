from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Messages(models.Model):
    MessageID = models.BigIntegerField(primary_key=True)
    UserIDFrom = models.CharField(max_length=25)
    UserIDTo = models.CharField(max_length=25)
    UserIDTo = models.DateTimeField()
    ProductID = models.BigIntegerField()
    MessageBody = models.TextField()

    def __str__(self):
        return self.MessageID


class Products(models.Model):
    ProductID = models.BigIntegerField(primary_key=True)
    UserID = models.BigIntegerField()
    ProductName = models.CharField(max_length=250)
    Price = models.PositiveSmallIntegerField()
    Pictures = models.ImageField()

    def __str__(self):
        return self.ProductID
