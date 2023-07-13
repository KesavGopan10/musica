from django.urls import path 
from  . import views 




urlpatterns = [
    path('',views.musicc,name="music"),
    path('music/<int:id>/' , views.musics , name="musics"),
]