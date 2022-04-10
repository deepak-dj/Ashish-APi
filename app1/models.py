from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
