#ADMİNLE İLGİLİ TÜM YÖNETİM İŞLERİ BURADA
from blog.models import Category, Blog, Images
from django.contrib import admin

#adminde ürün sayfasına girince fotoğraf eklenicek yer açıldı
class BlogImageInline(admin.TabularInline):
    model = Images #images tablosuna ait olucak
    extra = 5

# class tanımlıyoruz. bu kategori ile yapacağım ayarları
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']  # hangi alanlar görülsün istiyorum
    readonly_fields = ('image_tag',)
    list_filter = ['status']  # statuye göre filtreliyorum

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status'] # hangi alanlar görülsün istiyorum
    readonly_fields =('image_tag',)
    list_filter = ['status', 'category'] # statuye göre filtreliyorum
    inlines = [BlogImageInline] #blogimagesinline ürün ekleme sırasında istiyorsam burayada bağlantısını kurmalıyım
    '''blogla ilgili olduğu için sadece onunla alakalı şeyleri ekler
imageye class ekliyorum'''

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'blog']  # hangi alanlar görülsün istiyorum
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
# Register your models here.
#adminde images gözümesi için
admin.site.register(Images, ImagesAdmin) #sitede de gzükmesi için ımagesadminle bağlntı kuruyorum
