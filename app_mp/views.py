from django.shortcuts import render, redirect
from .models import song

def index(request):
  son = song.objects.all
  return render(request, 'app_mp/index.html', {'songs': son})