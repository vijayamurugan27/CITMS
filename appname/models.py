from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)    
    rollno = models.IntegerField()

    def __str__(self):
        return self.first_name
    

# from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    NoOfYears = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    )
    Stu_name = models.CharField(max_length = 200)
    department = models.CharField(max_length = 50)
    year = models.CharField(max_length = 1, choices = NoOfYears, default = 1)
    book = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    BookNumber = models.IntegerField()
    Issued_date = models.DateField(auto_now_add = True)
    returned  = models.BooleanField(default = False)
    returned_date = models.CharField(max_length = 20, null = True, blank = True)
    def __str__(self):
        return self.Stu_name

