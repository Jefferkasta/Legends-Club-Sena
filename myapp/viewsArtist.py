from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db import IntegrityError
import pytz
from loginUser.models import User
from .models import Artist, Appoinment
from django.contrib.auth.decorators import login_required

# para crear mensajes
from django.contrib import messages

@login_required
def profile(request):
    if request.user.artistUser == True:
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
        context =   {
            # 'users': users,
            # 'articles': articles,
            'appoinments': appoinments,
            }
        return render(request,'profileArtist.html', context)
    else:
        return render(request,'index.html')

@login_required
def createAppointment(request):  
    if request.user.artistUser == True:
        if request.method == 'POST':
            try:
                #trae la instancia del usuario
                userfound = User.objects.filter(identificationUser = request.POST['useridentification[]']).first()
                # trae el id del artista
                idUnformatedArtist = Artist.objects.filter(idUser__id=int(request.POST['idartist[]'])).values('id')
                idformatedArtist = idUnformatedArtist[0]['id']
                #trae la instancia del artista
                artistfound = Artist.objects.filter(id=idformatedArtist).first()
                # se guarda el registro en la base de datos
                Appoinment.objects.create(idUser = userfound,
                                    idArtist = artistfound,
                                    timeAppointment = request.POST['timeappointment[]'],
                                    descriptionAppointment = request.POST['descriptionappointment[]'],
                                    )
                messages.add_message(request, messages.SUCCESS, 'cita creada')
                return HttpResponse('cita creada',request)
            except IntegrityError as e:
                print("error ",f"IntegrityError: {e}")
                messages.add_message(request, messages.ERROR, 'correo admin ya existe')
                return HttpResponse("cita ya existe", request)
    else:
        return render(request,'index.html')
             
@login_required
def editAppoinment(request, id):
    if request.user.artistUser == True:
        if request.method == 'POST':
            # Obtiene la fecha y hora actual en UTC
            fecha_hora_utc = timezone.now()
            # Define la zona horaria de Colombia (UTC-5)
            zona_colombia = pytz.timezone('America/Bogota')
            # Convierte la fecha y hora actual de UTC a la zona horaria de Colombia
            fecha_hora_colombia = fecha_hora_utc.astimezone(zona_colombia)

            apponinmentUpdate = Appoinment.objects.get(id=id)
            apponinmentUpdate.descriptionAppointment = request.POST['txt-descriptionAppoinment']
            apponinmentUpdate.updatedAppointment = fecha_hora_colombia
            
            print(request.POST['txt-descriptionAppoinment'])
            apponinmentUpdate.save()
            return redirect("/profileArtist")
        else:
            return
    else:
        return render(request,'index.html')
        

@login_required
def deleteAppoinment(request, id):
    if request.user.artistUser == True:
        if request.method == 'POST':
            result = Appoinment.objects.filter(id=id).delete()
            print("ESTE "+result)
            return redirect("/profileArtist")
        else:
            return
    else:
        return render(request,'index.html')