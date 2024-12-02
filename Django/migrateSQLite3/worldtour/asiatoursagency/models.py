from django.db import models 

# Create your models here.

class Tour(models.Model) :
 
    originCountry = models.CharField(max_length = 64)
    distCountry   =  models.CharField(max_length = 64)
    numOfNigths   =  models.IntegerField()
    price         =  models.IntegerField()
    
    # this is a string representaion of the tours
    def __str__(self):
        return (f" ID {self.id} userName : {self.userName} Password : {self.password} -> Tour Detalis : From {self.originCountry} To {self.distCountry} , {self.numOfNigths} With A Price Of ${self.price}")
