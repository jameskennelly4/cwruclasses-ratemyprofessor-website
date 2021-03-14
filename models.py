from django.db import models
import csv

class Class(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100000)

class Professor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    link = models.CharField(max_length=2000)
    rating = models.CharField(max_length=50)
    class_taught1 = models.CharField(max_length=50, default='')
    class_taught2 = models.CharField(max_length=50, default='')
    class_taught3 = models.CharField(max_length=50, default='')
    class_taught4 = models.CharField(max_length=50, default='')
    class_taught5 = models.CharField(max_length=50, default='')
    class_taught6 = models.CharField(max_length=50, default='')

class Review(models.Model):
    name = models.CharField(max_length=50)
    class_reviewed = models.CharField(max_length=50)
    quality = models.FloatField(default=0)
    difficulty = models.FloatField(default=0)
    date = models.CharField(max_length=50)
    review_content = models.CharField(max_length=100000)

with open("/Users/jameskennelly/Desktop/mysite/Classes.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Class.objects.get_or_create(
                title=row[0],
                name=row[1],
                description=row[2],
                )

with open("/Users/jameskennelly/Desktop/mysite/Professors.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Professor.objects.get_or_create(
                firstname=row[0],
                lastname=row[1],
                link=row[2],
                rating=row[3],
                class_taught1=row[4],
                class_taught2=row[5],
                class_taught3=row[6],
                class_taught4=row[7],
                class_taught5=row[8],
                class_taught6=row[9],
                )

with open("/Users/jameskennelly/Desktop/mysite/Reviews.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Review.objects.get_or_create(
                name=row[0],
                class_reviewed=row[1],
                quality=row[2],
                difficulty=row[3],
                date=row[4],
                review_content=row[5],
                )
