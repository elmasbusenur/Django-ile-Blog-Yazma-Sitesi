from blog.models import Blog, Category
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage


# slider a gelen verileri buradan göndericem
# sorgu yapmamız gerekecek
#burada ki kısımlar anasayfayı dinamik hale getiriyor
def index(request):
    setting = Setting.objects.get(pk=1)  # primary key 1 i çağırıyor
    sliderdata = Blog.objects.all()[:3]  # get deseydik şart giricektik , :3 ürün al slider dataya at
    category = Category.objects.all()
    dayblogs = Blog.objects.all()[:4]
    lastblogs = Blog.objects.all().order_by('-id')[:1]
    randomblogs = Blog.objects.all().order_by('?')[:4] #random ürün seçiyoruz. 4 adet.


    context = {'setting': setting,
               'category': category,  # categorileri index sayfasına gönderiyoruz
               'page': 'home',
               'sliderdata': sliderdata, # sliderdata yı contexte yükledik
               'dayblogs': dayblogs,
               'lastblogs': lastblogs,
               'randomblogs': randomblogs,

               }
    return render(request, 'index.html', context)  # indexe gönderiyoruz


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
    form = ContactFormu()  # contact formu çağrıyoruz
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)  # ilettişim sayfasına formu gönderiyoruz


def category_blogs(request, id): #slug
    blogs = Blog.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    context = {'blogs': blogs,
               'category': category,
               'categorydata': categorydata
               }
    return render(request, 'blogs.html', context)
