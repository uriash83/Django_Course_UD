from django.db import models
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # po kliknięciu w submit w CreateSchool to jest adres do którego zostanie przekierowanie
    def get_absolute_url(self):
        return reverse("basicapp:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    # related_name ='students' jest wykorzystywany w school_detail.html w for loop

    def __str__(self):
        return self.name
