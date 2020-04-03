from blog.models import Category
from django.contrib import admin

#class tanımlıyoruz. bu kategori ile yapacağım ayarları
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status'] #hangi alanlar görülsün istiyorum
    list_filter = ["status"] # statuye göre filtreliyorum
admin.site.register(Category, CategoryAdmin)
# Register your models here.
