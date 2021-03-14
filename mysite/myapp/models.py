from django.db import models

class Class(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)

#class Teacher(models.Model):
#    firstname = models.CharField(max_length=50)
#    lastname = models.CharField(max_length=50)
#    rating = models.IntegerField(default=0)

#class Review(models.Model):
#    student = models.CharField(max_length=50)


#class Teaches(models.Model):

# Last one
