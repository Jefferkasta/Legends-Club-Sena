from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
# from django.contrib.auth import login, logout, authenticate
from loginUser.models import User
from .forms import formArtic
from .models import Article, Artist
# from django.contrib.auth import login, logout, authenticate

# para crear mensajes
from django.contrib import messages

def profile(request):
    print(request)
    users = User.objects.filter(adminUser=0)
    articles = list(Article.objects.values())
    artists = list(Artist.objects.values())
    context =   {
        'users': users,
        'articles': articles,
        'artists': artists,
        }
    messages.add_message(request, messages.SUCCESS, 'admin creado')
    return render(request,'profileAdmin.html', context)

def createSuperuser(request):
    if request.method == 'GET':  # ENVIANDO FORMULARIO
        print("")
    else:
        # return HttpResponse("admin creado", request)
        if request.POST['passwlogin[]'] == request.POST['confirmpasswlogin[]']:  # OBTENIENDO DATOS
            try:
                User.operation.create_superuser(identificationUser=request.POST['useridentification[]'],
                                                emailUser=request.POST['useremail[]'],
                                                firstnameUser=request.POST['userfirstname[]'],
                                                lastnameUser=request.POST['userlastname[]'],
                                                ageUser=request.POST['userage[]'],
                                                phoneUser=request.POST['userphone[]'],
                                                password=request.POST['passwlogin[]'])
                
                messages.add_message(request, messages.SUCCESS, 'admin creado')
                return HttpResponse("admin creado", request)
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'correo admin ya existe')
                return HttpResponse("correo admin ya existe", request)
            
def createArtist(request):  # LOGIN - REGISTRO
        if request.method == 'POST':  # OBTENIENDO DATOS
            try:
                # print("este ",request.POST);
                userfound = User.objects.filter(identificationUser = request.POST['artistidentification[]']).first()
                artist = Artist.objects.create(idUser = userfound,
                                   stileTattoArtist = request.POST['artistestile[]'],
                                   experienceArtist = request.POST['artistexperience[]'],
                                   nationalityArtist = request.POST['artistnationality[]'],
                                   )
                messages.add_message(request, messages.SUCCESS, 'admin creado')
                return JsonResponse({'response':"artista creado"})
            except IntegrityError as e:
                print("error ",f"IntegrityError: {e}")
                messages.add_message(request, messages.ERROR, 'correo admin ya existe')
                return HttpResponse("correo artista ya existe", request)
    
def deleteArtist(request, id):
    if request.method == 'POST':
        result = Artist.objects.filter(id=id).delete()
        print("ESTE "+result)
        return redirect("/profileAdmin")
    else:
        return

def crea_articulos(request):
    if request.method == 'GET':
        print("ENTRA SOLO AL GETTTTTTTT :O")
        return render(request, 'crea_articulos.html', {
            'form': formArtic
        })
        
    else:
        print("ENTRA AL POST <3") 
        form = formArtic(request.POST)
        new_artic = form.save(commit=False)
        new_artic.user = request.user
        new_artic.save()
        return redirect('articulos')
      
def articulos(request):  # TRAE LOS DATOS DE LA TABLA ARTICULOS
    articulo = list(Article.objects.values())
    return JsonResponse(articulo, safe=False)

def editUser(request, id):
    if request.method == 'POST':
        # data = {
        #     firstnameUser = request.POST['txt-userfirstname'],
        #     lastnameUser = request.POST['txt-userlastname'],
        #     ageUser = request.POST['txt-userage'],
        #     phoneUser = request.POST['txt-userphone'],
        # }
        # query = User.objects.filter(id=id).update()
        # print(query)
        return redirect("/profileAdmin")
    else:
        return
    
def deleteUser(request, id):
    if request.method == 'POST':
        result = User.objects.filter(id=id).delete()
        print(result)
        return redirect("/profileAdmin")
    else:
        return
        
    