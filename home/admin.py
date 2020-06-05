from django.contrib import admin

# Register your models here.
#home/models deki clasın migrations dan sonra çalışabilmesi için register yapmalıyız.
from home.models import Setting
admin.site.register(Setting)