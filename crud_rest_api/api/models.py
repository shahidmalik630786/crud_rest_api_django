from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    city=models.CharField(max_length=70)

    class Meta:
        db_table="Student"
