from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)  # foreignkey self kendi id sine refere edicek
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def image_tag(self):   #image diye html kodu yazıyoruz adı img tag.class image in altında ki image burada ki image url kısmı search kısmına yazılıyor
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'




class Blog(models.Model):  # kategori ile ilişki kuruyoruz
    STATUS = [
        ('True', 'Evet'),
        ('False', 'Hayır'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # foreignkey kategori: kategoriye refere ettik
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):   #image diye html kodu yazıyoruz adı img tag.class image in altında ki image burada ki image url kısmı search kısmına yazılıyor
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


# ilk olarak ilişki kuracağım alanı yzıyorum blog tablosu..cascade= on delete durumunda (drapdown)ilişkili olduğu
# product silinirse buda silinmeli bağlı olduğu şey silinirse alt alan havada kalır oda silinmeli

class Images(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)  # blankTrue dersek etiketi boş geçmemize izin verir
    image = models.ImageField(blank=True, upload_to='images/')

    # bu değişikliği yaptıktan sonra veritabanında migrate etmek gerekir
    # python manage.py makemigrations  şu dosyayı oluşturdum
    # python manage.py migrate ile de migrate ediyorum veri tabanına işliyor
    # veritabanında title image bolog_id oluştu
    # django frameworkte id ler otomatik oluşur

    # bu model ne döndersin..veritabanında şimdi ürünlerin ismi gözüküyor
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

