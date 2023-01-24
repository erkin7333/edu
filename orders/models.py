from django.db import models
from main.models import Courses
from account.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.BigIntegerField()
    order_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.total_price} {self.order_at}"


class OrderCourses(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    quantity = models.IntegerField()
