from django.urls import path
from . import views
from . import viewsAdmin

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'), 
    path('agendarCita/', views.agendarCita, name='agendarCita'),
    path('detail-artist/', views.detailArtist), #hptta
    path('profileAdmin/', viewsAdmin.profile),
    path('profileAdmin/<int:id>', viewsAdmin.deleteUser, name='deleteUser'),
    path('profileAdmin/<int:id>', viewsAdmin.editUser, name='editUser'),
    path('profileAdmin/new-superuser/', viewsAdmin.createSuperuser),
    path('profileAdmin/new-artista/', viewsAdmin.createArtist),
    path('articulos/', viewsAdmin.articulos, name='articulos'),  # URL-VISTA//MUESTRA DATOS TABLA ARTICULOS    
    path('articulos/crea_articulos/', viewsAdmin.crea_articulos, name='crea_articulos'),  # URL-VISTA// CREA ARTICULOS
    
]
