from django.urls import path
from authapp import views
urlpatterns = [
    path('register/',views.Register, name='register' ),
    path('login/',views.Login, name='login' ),
    path('logout/',views.Logout, name='logout' ), 
    path('edit_registration/',views.edit_registration, name='edit_registration' ), 
    path('change_password/',views.change_password, name='change_password' ), 
]