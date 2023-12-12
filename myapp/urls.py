from django.urls import path
from . import views
from . import viewsAdmin
from . import viewsArtist
# from . import viewsUser

urlpatterns = [
    # url General
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('detail-artist/', views.detailArtist,name='detailartist'),
    path('profileUser/', views.profileUser,name='profileUser'),
    # url profileAdmin
    path('profileAdmin/', viewsAdmin.profile, name='profileadmin'),
    path('profileAdmin/edit-user/<int:id>/', viewsAdmin.editUser, name='editUser'),
    path('profileAdmin/delete-user/<int:id>/', viewsAdmin.deleteUser, name='deleteUser'),
    path('profileAdmin/new-superuser/', viewsAdmin.createSuperuser,name='newsuperuser'),
    path('profileAdmin/new-artist/', viewsAdmin.createArtist, name='newartist'),
    path('profileAdmin/edit-artist/<int:id>/', viewsAdmin.editArtist, name='editArtist'),
    path('profileAdmin/delete-artist/<int:id>/', viewsAdmin.deleteArtist, name='deleteArtist'),
    # url profileArtist
    path('profileArtist/', viewsArtist.profile),
    path('profileArtist/new-appointment/', viewsArtist.createAppointment, name='newappointment'),
    path('profileArtist/delete-appoinment/<int:id>/', viewsArtist.deleteAppoinment, name='deleteAppoinment'),
    path('profileArtist/edit-appoinment/<int:id>/', viewsArtist.editAppoinment, name='editAppoinment'),
    path('profileAdmin/new-article/', viewsAdmin.createArticle, name='newarticle'),
    path('profileArtist/edit-article/<int:id>/', viewsAdmin.editArticle, name='editArticle'),
    path('profileArtist/delete-article/<int:id>/', viewsAdmin.deleteArticle, name='deleteArticle'),
    path('stylestattoo/', views.stylesTattoo, name='stylesTattoo'),
]


