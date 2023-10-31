from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('store:wikipedia_link', args=[self.name])

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('store:course', args=[self.name])

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

class Order(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    mail = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    purpose = models.CharField(max_length=100)
    materials_provided = models.ManyToManyField(Material)

    def __str__(self):
        return '{}'.format(self.name)



