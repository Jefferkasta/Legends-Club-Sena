from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from loginUser.models import User
from .models import Article, Artist, Appoinment
from django.contrib.auth.decorators import login_required

# para crear mensajes
from django.contrib import messages

@login_required
def profile(request):
    if request.user.adminUser == True:
        users = User.objects.filter(adminUser=0)
        articles = list(Article.objects.values())
        #consultas con inner join Django
        artists = Artist.objects.select_related('idUser').values('id','idUser__identificationUser','idUser__firstnameUser','idUser__lastnameUser', 'experienceArtist', 'nationalityArtist', 'stileTattoArtist', 'idUser__phoneUser','activeArtist')
        # artists = Artist.objects.filter(idUser__emailUser=request.POST.get('txt-useremail')).values('id','idUser__identificationUser','idUser__firstnameUser','idUser__lastnameUser', 'experienceArtist', 'nationalityArtist', 'stileTattoArtist','activeArtist', 'idUser__phoneUser')
        # usuarios_con_perfil = User.objects.select_related('id').all()
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
            'appoinments': appoinments,
            'users': users,
            'articles': articles,
            'artists': artists,
            }
        for article in articles:

            print(article['imageArticle'])

        messages.add_message(request, messages.SUCCESS, 'admin creado')
        return render(request,'profileAdmin.html', context)
    else:
        return render(request,'index.html')

@login_required
def createSuperuser(request):
    if request.user.adminUser == True:
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
    else:
        return render(request,'index.html')


@login_required
def editUser(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            userUpdate = User.objects.get(id=id)
            userUpdate.firstnameUser = request.POST['txt-userfirstname']
            userUpdate.lastnameUser = request.POST['txt-userlastname']
            userUpdate.ageUser = request.POST['txt-userage']
            userUpdate.phoneUser = request.POST['txt-userphone']
            
            userUpdate.save()
            return redirect("/profileAdmin")
        else:
            return
    else:
        return render(request,'index.html')
        

@login_required    
def deleteUser(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            result = User.objects.filter(id=id).delete()
            print(result)
            return redirect("/profileAdmin")
        else:
            return
    else:
        return render(request,'index.html')
        
        
@login_required
def createArtist(request):  # LOGIN - REGISTRO
    if request.user.adminUser == True:
        if request.method == 'POST':  # OBTENIENDO DATOS
            try:
                #consulta tabla del usuario segun el filtro y le asigna 1 al campo artistUser
                user = User.objects.filter(identificationUser = request.POST['artistidentification[]']).first()
                user.artistUser = 1
                user.save()
                userfound = User.objects.filter(identificationUser = request.POST['artistidentification[]']).first()
                print(user)
                Artist.objects.create(idUser = userfound,
                                    stileTattoArtist = request.POST['artistestile[]'],
                                    experienceArtist = request.POST['artistexperience[]'],
                                    nationalityArtist = request.POST['artistnationality[]'],
                                    )
                messages.add_message(request, messages.SUCCESS, 'admin creado')
                return JsonResponse("artista creado", request)
            except IntegrityError as e:
                print("error ",f"IntegrityError: {e}")
                messages.add_message(request, messages.ERROR, 'correo admin ya existe')
                return HttpResponse("correo artista ya existe", request)
    else:
        return render(request,'index.html')
    
        
@login_required
def editArtist(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            artistUpdate = Artist.objects.get(id=id)
            artistUpdate.experienceArtist = request.POST['txt-experienceArtist']
            artistUpdate.nationalityArtist = request.POST['txt-nationalityArtist']
            artistUpdate.stileTattoArtist = request.POST['txt-stileTattoArtist']
            
            artistUpdate.save()
            return redirect("/profileAdmin")
        else:
            return
    else:
        return render(request,'index.html')
        

@login_required
def deleteArtist(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            result = Artist.objects.filter(id=id).delete()
            return JsonResponse("artista creado", request)
        else:
            return
    else:
        return render(request,'index.html')
    

@login_required 
def createArticle(request):
    if request.user.adminUser == True:
        if request.method == 'POST':
            try:
                article = Article.objects.create(
                    imageArticle = request.FILES['file-imageArticle'],
                    nameArticle = request.POST['txt-nameArticle'],
                    categoryArticle = request.POST['txt-categoryArticle'],
                    descriptionArticle = request.POST['txt-descriptionArticle'],
                    priceArticle = request.POST['txt-priceArticle'])
                
                article.save()
                messages.add_message(request, messages.SUCCESS, 'producto creado')
                # return JsonResponse("producto creado", request)
                return redirect("/profileAdmin")
            except IntegrityError as e:
                print("error ",f"IntegrityError: {e}")
                messages.add_message(request, messages.ERROR, 'Ese producto ya existe')
                return HttpResponse("Ese producto ya existe", request)
    else:
        return render(request,'index.html')
        
@login_required
def editArticle(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            articleUpdate = Article.objects.get(id=id)
            articleUpdate.nameArticle = request.POST['txt-nameArticle']
            articleUpdate.categoryArticle = request.POST['txt-categoryArticle']
            articleUpdate.descriptionArticle = request.POST['txt-descriptionArticle']
            articleUpdate.priceArticle = request.POST['txt-priceArticle']
            
            articleUpdate.save()
            return redirect("/profileAdmin")
        else:
            return
    else:
        return render(request,'index.html')
        

@login_required
def deleteArticle(request, id):
    if request.user.adminUser == True:
        if request.method == 'POST':
            Article.objects.filter(id=id).delete()
            return JsonResponse("producto eliminado", request)
        else:
            return
    else:
        return render(request,'index.html')
    
        