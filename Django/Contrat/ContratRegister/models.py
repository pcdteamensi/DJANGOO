from django.db import models

# Create your models here.
class Contrat(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,blank=True, null=True, unique=True, default=None)
    password = models.CharField(max_length=20,default=None)
    adresse = models.CharField(max_length=20,default=None)
    date_debut_contrat = models.DateTimeField(default=None)
    date_fin_contrat=models.DateTimeField(default=None)
    type_pack=models.CharField(max_length=10,default=None)



    def __str__(self):
         return self.email
