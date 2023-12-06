from django.urls import path
from . import views
from . import viewsAdmin
from . import viewsUser

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'), 
    path('agendarCita/', views.agendarCita, name='agendarCita'),
    path('detail-artist/', views.detailArtist),
    path('profileAdmin/<int:usuario_id>/', viewsAdmin.profile),
    path('profileAdmin/<int:id>', viewsAdmin.deleteUser, name='deleteUser'),
    path('profileAdmin/<int:id>', viewsAdmin.editUser, name='editUser'),
    path('profileAdmin/new-superuser/', viewsAdmin.createSuperuser),
    path('profileAdmin/new-artista/', viewsAdmin.createArtist),
    path('profileAdmin/<int:id>', viewsAdmin.deleteArtist, name='deleteArtist'),
    path('articulos/', viewsAdmin.articulos, name='articulos'),   
    path('articulos/crea_articulos/', viewsAdmin.crea_articulos, name='crea_articulos'),
    #path('profileUser/<int:usuario_id>/', viewsUser.detalle_usuario, name='profileUser'),
    #path('profileUser/<int:usuario_id>/', viewsUser.detalle_usuario, name='detalle_usuario'),
    
]
