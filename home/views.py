from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting
def index(request):
    setting = Setting.objects.get(pk=1) #primary key 1 i çağırıyor
    context = {'setting': setting}
    return render(request, 'index.html', context)
#contexte ekledik ve index html e gönderdik ve index html de istediğimiz yere istediğimiz bilgileri yazdık
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)
