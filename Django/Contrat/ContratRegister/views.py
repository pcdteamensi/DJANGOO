from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Contrat

def register(request):

    return render(request,'ContratRegister/login.html')
def register_form(request):
    nom = request.POST["nom"]
    prenom = request.POST["prenom"]
    email = request.POST["email"]
    password = request.POST["password"]
    adresse = request.POST["adresse"]
    date_debut_contrat = request.POST["date_debut_contrat"]
    date_fin_contrat=request.POST["date_fin_contrat"]
    type_pack=request.POST["type_pack"]
    c=Contrat(nom=nom,prenom=prenom,email=email,password=password,adresse=adresse,date_debut_contrat=date_debut_contrat,date_fin_contrat=date_fin_contrat,type_pack=type_pack)
    c.save()
    return render(request,'ContratRegister/login.html')
def log_in_page(request):

         context={}
         if request.method =="POST":
           email=request.POST['email']
           password=request.POST['password']
           print("request post cv if loula yodkhleleha ")
           if (Contrat.objects.filter(email__startswith=email) and Contrat.objects.filter(password__startswith=password)):

                  print("if 2 yodkhlelha")
                  Contrat.objects.filter(email=email).delete()

                  return render(request, 'ContratRegister/login.html')
           else:
              context["error"]="Entrer des coordonnées valides"
              print("el if tal log in mayod5lelhech")
              return render(request, 'ContratRegister/loginverif.html', context)
         else:
              print("if loula mayodkhlelhech")
              return  render(request,'ContratRegister/loginverif.html',context)
