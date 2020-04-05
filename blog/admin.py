from blog.models import Category, Blog
from django.contrib import admin


# class tanımlıyoruz. bu kategori ile yapacağım ayarları
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']  # hangi alanlar görülsün istiyorum
    list_filter = ['status']  # statuye göre filtreliyorum
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'title', 'amount', 'status']  # hangi alanlar görülsün istiyorum
    list_filter = ['status','category']  # statuye göre filtreliyorum


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
# Register your models here.
