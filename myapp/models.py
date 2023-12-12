from django.db import models
# from datetime import datetime, timezone 
from django.utils import timezone
from loginUser.models import User
# Create your models here.

class Artist(models.Model):
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    stileTattoArtist = models.CharField(max_length=80, null = True)
    experienceArtist = models.CharField(max_length=3, null = True)
    nationalityArtist = models.CharField(max_length=80, null = True)
    createdArtist = models.DateTimeField(default=timezone.now, blank=True)
    updatedArtist = models.DateTimeField(null=True, blank=True)
    activeArtist = models.BooleanField(default = True)


    objects = models.Manager()
    
    # def __str__(self):
    #     return str(self.stileTattoArtist, self.nationalityArtist)
    
class Appoinment(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False) # PRIMARY KEY tbUsuarios !!!!ERROR AL CREAR DATO EN LA TABLA !!!- 
    idArtist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False, blank=False) # PRIMARY KEY tbUsuarios !!!!ERROR AL CREAR DATO EN LA TABLA !!!- 
    timeAppointment = models.CharField(max_length=10)
    descriptionAppointment = models.TextField()
    dateAppointment = models.DateTimeField(auto_now_add=True)
    updatedAppointment = models.DateTimeField(blank=True, null=True)
    createdAppointment = models.DateTimeField(default=timezone.now, blank=True)
    activeAppointment = models.BooleanField(default = True)
    
    objects = models.Manager()

    # def __str__(self):
    #     return str()

class Article(models.Model):
    imageArticle = models.ImageField(upload_to='products/',max_length=200, blank=True, null=True)
    nameArticle = models.CharField(max_length=50)
    categoryArticle = models.TextField()
    descriptionArticle = models.TextField()
    priceArticle = models.IntegerField()
    updatedArticle = models.DateTimeField(blank=True, null=True)
    createdArticle = models.DateTimeField(default=timezone.now, blank=True)
    activeArticle = models.BooleanField(default = True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.nameArticle)

    
