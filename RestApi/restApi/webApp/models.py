from django.db import models

# Create your models here.

class employees(models.Model):
    firstName= models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    Emp_id=models.IntegerField()
    def __str__(self):
        return self.firstName


class students(models.Model):
    firstName= models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    Stu_id=models.IntegerField()
    def __str__(self):
        return self.firstName

