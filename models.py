from django.db import models
from django.contrib.auth.models import User 



class Status(models.Model):
    name = models.CharField(max_length = 55) 
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length = 55) 
    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 255)
    date_of_birth = models.DateField() 
    age = models.PositiveIntegerField() 
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE) 
    status = models.ForeignKey(Status, on_delete=models.CASCADE) 
    email = models.EmailField() 
    phone = models.PositiveIntegerField() 
    address = models.CharField(max_length = 255)
    citizenship_number = models.PositiveIntegerField(null = True, blank = True)
    home_phone_number = models.PositiveIntegerField(null = True, blank = True)  
    emp_code = models.IntegerField() 
    joined_date = models.DateField()  
    department = models.CharField(max_length = 55, default = "") 
    position = models.CharField(max_length = 55) 
    salary = models.PositiveBigIntegerField() 
    bio = models.TextField(max_length = 1000, null = True, blank = True)
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)
    
    @property 
    def imageURL(self):
        try: 
            url = self.image.url 
        except: 
            url = '' 
        return url 

    def __str__(self):
        return self.full_name 
