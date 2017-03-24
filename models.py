from django.db import models

class Campus_drive(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):              
        return self.name

class student_id(models.Model):
    student_id = models.ForeignKey(student_id, on_delete=models.CASCADE)
    date_joined = models.DateField()
