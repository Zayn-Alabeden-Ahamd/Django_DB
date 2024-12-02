from django.db import models

# Create your models here.
class Log(models.Model):
    #userName
    userName = models.CharField(max_length=64)
    #email
    email = models.CharField(max_length=120)
    #password
    password = models.CharField(max_length=64)

    def __str__(self):
        return (f"ID : {self.id}  User_Name Is {self.userName} With Em@il : {self.email} And Password Of {self.password}")