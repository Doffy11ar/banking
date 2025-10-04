from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
            return f"{self.name} {self.abrev} {self.status}"


class Departments(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='id_country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

class Cities(models.Model):
    id_department = models.ForeignKey(Departments, on_delete=models.CASCADE, db_column='id_departments')
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)  
    email = models.EmailField(max_length=100, unique=True)  
    address = models.CharField(max_length=255, blank=True) 
    password = models.CharField(max_length=255)
    id_city = models.IntegerField(null=True, blank=True) 
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    



    