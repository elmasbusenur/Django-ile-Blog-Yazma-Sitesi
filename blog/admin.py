#ADMİNLE İLGİLİ TÜM YÖNETİM İŞLERİ BURADA
from blog.models import Category, Blog, Images
from django.contrib import admin

#adminde ürün sayfasına girince fotoğraf eklenicek yer açıldı
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class BlogImageInline(admin.TabularInline):
    model = Images #images tablosuna ait olucak
    extra = 5

# class tanımlıyoruz. bu kategori ile yapacağım ayarları
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']  # hangi alanlar görülsün istiyorum
    readonly_fields = ('image_tag',)
    list_filter = ['status']  # statuye göre filtreliyorum

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status','category'] # hangi alanlar görülsün istiyorum
    readonly_fields =('image_tag',)
    list_filter = ['status', 'category'] # statuye göre filtreliyorum
    inlines = [BlogImageInline] #blogimagesinline ürün ekleme sırasında istiyorsam burayada bağlantısını kurmalıyım
    '''blogla ilgili olduğu için sadece onunla alakalı şeyleri ekler
imageye class ekliyorum'''

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'blog']  # hangi alanlar görülsün istiyorum
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_blogs_count', 'related_blogs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative blog count
        qs = Category.objects.add_related_count(
                qs,
                Blog,
                'category',
                'blogs_cumulative_count',
                cumulative=True)

        # Add non cumulative blog count
        qs = Category.objects.add_related_count(qs,
                 Blog,
                 'category',
                 'blogs_count',
                 cumulative=False)
        return qs

    def related_blogs_count(self, instance):
        return instance.blogs_count
    related_blogs_count.short_description = 'Related blog (for this specific category)'

    def related_blogs_cumulative_count(self, instance):
        return instance.blogs_cumulative_count
    related_blogs_cumulative_count.short_description = 'Related blog (in tree)'
"""""
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','blog','user','status']
    list_filter = ['status']
"""""
admin.site.register(Category, CategoryAdmin2)
admin.site.register(Blog, BlogAdmin)
# Register your models here.
#adminde images gözümesi için
admin.site.register(Images, ImagesAdmin) #sitede de gzükmesi için ımagesadminle bağlntı kuruyorum
