from django.urls import path
from . import views
from . import viewsAdmin
# from . import viewsUser

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('agendarCita/', views.agendarCita, name='agendarCita'),
    path('detail-artist/', views.detailArtist,name='detailartist'),
    # path('profileAdmin/<int:usuario_id>/', viewsAdmin.profile, name='profileadmin'),
    path('profileAdmin/', viewsAdmin.profile, name='profileadmin'),
    path('profileAdmin/delete/<int:id>/', viewsAdmin.deleteUser, name='deleteUser'),
    path('profileAdmin/edit/<int:id>/', viewsAdmin.editUser, name='editUser'),
    path('profileAdmin/new-superuser/', viewsAdmin.createSuperuser,name='newsuperuser'),
    path('profileAdmin/new-artista/', viewsAdmin.createArtist, name='newartist'),
    path('profileAdmin/delete-artist/<int:id>/', viewsAdmin.deleteArtist, name='deleteArtist'),
    path('articulos/', viewsAdmin.articulos, name='articulos'),   
    path('articulos/crea_articulos/', viewsAdmin.crea_articulos, name='crea_articulos'),
    
]
