from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from loginUser.models import User
from .models import Appoinment
from django.views.generic import TemplateView


# Create your views here.
# class PageNotFound(TemplateView):
#     pagenotfound = '404.html'
    
# class PageErrorFound(TemplateView):
#     pageerrorfound = '404.html'

def home(request):      #  HOME
    return render(request, 'index.html')

def signup(request):  #  REGISTRO

    if request.method == 'GET':  # ENVIANDO FORMULARIO
        return render(request, 'signup-main.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['txt-passwlogin'] == request.POST['txt-confirmpasswlogin']:  # OBTENIENDO DATOS
            try:
                user = User.operation.create_user(identificationUser=request.POST['txt-useridentification'],
                                                emailUser=request.POST['txt-useremail'],
                                                firstnameUser=request.POST['txt-userfirstname'],
                                                lastnameUser=request.POST['txt-userlastname'],
                                                ageUser=request.POST['txt-userage'],
                                                phoneUser=request.POST['txt-userphone'],
                                                password=request.POST['txt-passwlogin'])
                
                user = User.objects.get(emailUser=request.POST.get('txt-useremail'))
                if user.adminUser:
                    login(request, user)
                    return redirect('/profileAdmin')
                else :
                    if user.artistUser:
                        login(request, user)
                        return redirect('/profileArtist')
                    else:
                        login(request, user)
                        return redirect('/profileUser')
            except IntegrityError:
                return render(request, 'signup-main.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists - Nombre de usuario ya existe'
                })

        return render(request, 'signup-main.html', {
            'form': UserCreationForm,
            "error": 'Password do not match - Contraseña no coinciden'
        })

def signout(request):  #  CIERRA SESION
    logout(request)
    return redirect('/')

def signin(request):  #  INICIA SESION
    if request.method == 'GET':
        return render(request, 'signin-main.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, emailUser=request.POST['txt-useremail'], password=request.POST['txt-passwlogin'])
        if user is None:
            return render(request, 'signin-main.html', {
                'form': AuthenticationForm,
                'error': 'Correo o contraseña es incorrecta'
            })
        else:
            user = User.objects.get(emailUser=request.POST.get('txt-useremail'))
            if user.adminUser:
                login(request, user)
                return redirect('/profileAdmin')
            else :
                if user.artistUser:
                    login(request, user)
                    return redirect('/profileArtist')
                else:
                    login(request, user)
                    return redirect('/profileUser')
                
@login_required
def profileUser(request):
    appoinmentsUnformated = Appoinment.objects.select_related('idUser', 'idArtist').all()
    appoinments = []
    for row in appoinmentsUnformated:
        appointmentDict = {
            'id' : row.id,
            'identificationUser' : row.idUser.identificationUser,
            'nameUser' : row.idUser.firstnameUser+' '+ row.idUser.lastnameUser,
            'dateAppoinment' : row.timeAppointment,
            'descriptionAppoinment' : row.descriptionAppointment,
            'nameArtist' : row.idArtist.idUser.firstnameUser+'\n'+row.idArtist.idUser.lastnameUser,
            'phoneUser' : row.idUser.phoneUser,
            'emailUser' : row.idUser.emailUser
        }
        appoinments.append(appointmentDict)
    return render(request,'profileUser.html', {'appoinments': appoinments,})

def detailArtist(request):
    return render(request,'detail-artist.html')

def stylesTattoo(request):      #  styles Tattoo
    return render(request, 'styles.html')

# ------------ SUPER USUARIO -------------#
# USUARIO = JFR
# CORREO = jeferkasta@hotmail.com
# CONTRASEÑA = 64c8....

# CORREO = JFRAdmin@gmail.com
# CONTRASEÑA = 12345jfr
