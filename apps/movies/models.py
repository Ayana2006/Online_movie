from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=35)
    slug = models.SlugField(verbose_name='Понятный для', max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
              
class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    slug = models.SlugField('Понятный для', max_length=255, unique=True)
    description = models.CharField('Описание фильма',max_length=500)
    poster = models.ImageField('Постер фильма',upload_to="movie_poster/")
    trailer  = models.URLField('Трейлер')
    movie = models.FileField('Посмотреть фильм',upload_to='movie_video/')
    year = models.DateField("Дата выпуска", default=0)
    running_time = models.CharField('Длительность фильма', max_length=10)
    country = models.CharField("Страна",max_length=200)
    category = models.ForeignKey(Category,verbose_name = 'Категории',  on_delete=models.SET_NULL, null=True)
    directors = models.CharField("Режиссёры", max_length=555)
    actors = models.CharField("Актёры", max_length=50000, null=True, blank=True)
    genres = models.CharField('Жанры', max_length=255)
    rating = models.FloatField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        
class Photomovie(models.Model):
    image = models.ImageField(upload_to='images/')
    movie = models.ForeignKey(Movie, related_name='gallery', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.movie.title
    
    class Meta:
        verbose_name = "Галерея фильмов"
        verbose_name_plural = "Галерея фильмов"

class Series(models.Model):
    series = models.ForeignKey(Movie, related_name='series', on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/')
    
    def __str__(self):
        return self.series.title
    
    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"
