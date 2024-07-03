from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class users(models.Model):
    mobile=models.CharField(default='',unique=True,max_length=10)
    name=models.CharField(default='',max_length=50,null=False)
    password=models.CharField(default='',max_length=8,null=False)
class courses(models.Model):
    name=models.CharField(default='',max_length=50,null=False)
    duration=models.CharField(default=30)
    fee=models.CharField(default=5000)
    is_active=models.BooleanField(default=True)
    course_id=models.CharField(max_length=20)
class leads(models.Model):
    user_name=models.CharField(default='',max_length=50,null=False)
    mail=models.EmailField(default='')
    mobile=models.CharField(default='',max_length=10,null=False)
    course_id=models.CharField(default='',max_length=50,null=False)
    date_of_visit=models.DateField()
    source=models.CharField(default='',max_length=100)
    status=models.CharField(default='',max_length=50)
    mode=models.CharField(default='',max_length=50)

class Trainers(models.Model):

    mobile = models.CharField(default='', unique=True, max_length=10)
    name = models.CharField(default='', max_length=50, null=False)
    course_id = models.CharField(default='', max_length=50, null=False)
    trainer_id = models.CharField(default='', max_length=50, null=False)
class Batches(models.Model):
    Batch_id=models.CharField(default='')
    start_date=models.DateField()
    end_date=models.DateField()
    course_id=models.CharField(default='', max_length=50, null=False)
    trainer_id=models.CharField(default='', max_length=50, null=False)
    status=models.CharField(default='',max_length=50)
    leads = ArrayField(
        models.CharField(max_length=10, blank=True,default=''),
    )

class students(models.Model):


    mobile = models.CharField(max_length=10)
    name = models.CharField( max_length=50, null=False)
    email= models.CharField( max_length=50, null=False)
    Batch_id=models.CharField(max_length=50, null=False)
    course_id = models.CharField(default='', max_length=50, null=False)
    status = models.CharField(default='', max_length=50)
    fee = models.CharField(default=5000)
    paid=models.CharField(default='')
    pending=models.CharField(default='')
class payments(models.Model):
    student_id=models.CharField(default='', max_length=50, null=False)
    Batch_id = models.CharField(default='', max_length=50, null=False)
    Amount=models.CharField(default='')
    date_of_payment=models.DateField()



