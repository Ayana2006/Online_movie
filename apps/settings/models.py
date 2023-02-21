from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155,  null=True)
    litle_title = models.CharField(max_length=100,  null=True)
    description = models.TextField(max_length=555,  null=True)
    bg = models.FileField(upload_to='bg/')
    logo = models.FileField(upload_to='logo/')
    phone = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    graphic = models.CharField(max_length=50,  null=True)
    facebook = models.URLField()
    instagram = models.URLField()
    tiktok = models.URLField()
    twitter = models.URLField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
class Privacy(models.Model):
    title = models.CharField(max_length=250, null=True )
    litle_text = models.CharField(max_length=350, null=True)
    text_1 = models.TextField(max_length=10000, null=True)
    text_2 = models.TextField(max_length=10000, null=True)
    text_3 = models.TextField(max_length=10000, null=True)
    text_4 = models.TextField(max_length=10000, null=True)
    text_5 = models.TextField(max_length=10000, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'
        
    
class About(models.Model):
    title = models.CharField(max_length=55, null=True)
    litle_text = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=10000, null=True)
   
    def __str__(self):
       return self.title
    
    class Meta:
        verbose_name = 'О кинотеатре'
        verbose_name_plural = 'О кинотеатре'
    
class Media(models.Model):
    image = models.ImageField(upload_to='images/')
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='media')
    
    def __str__(self):
        return self.about.title
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        
class Partners(models.Model):
    title = models.CharField(max_length=155, null=True)
    text = models.CharField(max_length=555, null=True)
    
    def __str__(self):
       return self.title
    
    class Meta:
        verbose_name = 'Наши партнеры'
        verbose_name_plural = 'Наши партнеры'

class PartnersImage(models.Model):
    image = models.ImageField(upload_to='images/')
    link = models.URLField()
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='image')
    
    def __str__(self):
        return self.partner.title
    
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        
class Contact(models.Model):
    name = models.CharField(max_length=55)
    subject = models.CharField(max_length=222)
    text = models.TextField(max_length=3333)
    email = models.EmailField()
    phone = models.CharField(max_length=55,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        




