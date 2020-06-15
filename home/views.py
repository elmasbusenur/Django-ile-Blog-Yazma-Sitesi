from blog.models import Blog, Category
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage

#slider a gelen verileri buradan göndericem
#sorgu yapmamız gerekecek
def index(request):
    setting = Setting.objects.get(pk=1)  # primary key 1 i çağırıyor
    sliderdata = Blog.objects.all()[:3] #get deseydik şart giricektik , :3 ürün al slider dataya at
    category = Category.objects.all()

    context = {'setting': setting,
               'category': category, #categorileri index sayfasına gönderiyoruz
               'page' : 'home',
               'sliderdata':sliderdata } #sliderdata yı contexte yükledik
    return render(request, 'index.html', context) #indexe gönderiyoruz


# contexte ekledik ve index html e gönderdik ve index html de istediğimiz yere istediğimiz bilgileri yazdık
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildi mi. edilmezse setting e iner.
        form = ContactFormu(request.POST)  # CONTACT FORMUNU POSTLA EŞLEŞTİR
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarıyla gönderilmiştir. Teşekkür Ederiz")
            return HttpResponseRedirect('/iletisim')  # formu iletişim sayfasına gönderiyoruz

    setting = Setting.objects.get(pk=1)
    form = ContactFormu() #contact formu çağrıyoruz
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context) #ilettişim sayfasına formu gönderiyoruz
