from django.shortcuts import render, redirect
from .models import song
from .forms import MemberForm
from django.contrib import messages

def index(request):
  son = song.objects.all
  return render(request, 'app_mp/index.html', {'songs': son})


def add(request):
  if request.method == 'POST':
    form = MemberForm(request.POST or None)
    if form.is_valid():
      form.save()
    else:
      messages.success(request, (' There was an error '))
    messages.success(request, (' Your song detail has been sumbitted successfully! '))
    return render(request, 'app_mp/add.html', {})

  else:  
    return render(request, 'app_mp/add.html', {})