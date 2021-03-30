from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title  = models.CharField(max_length=255)
    url = models.URLField()
    pub_date = models.DateField()
    image = models.ImageField()
    icon = models.ImageField()
    votes = models.IntegerField(default=0)
    body = models.TextField()
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]