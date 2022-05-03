from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey("account.MyUser", related_name='orders', on_delete=models.CASCADE)