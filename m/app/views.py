from django.shortcuts import render
from .models import music 
# Create your views here.

def musicc(request):
    form = music.objects.all()
    return render ( request , 'app/music.html'    , { 'form' : form } )


def musics (request , id = id ):
    form = music.objects.filter( id = id ).first()
    print( form.t)
    return render ( request , 'app/mucics.html' , { 'form' : form })
