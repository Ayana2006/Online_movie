from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.movies.models import Movie

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.FileField(upload_to='profile_image/')
    email = models.EmailField(verbose_name="Почта")
    
    def __str__(self):
        return  self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
class Comments(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='user_comment',on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_comment',on_delete = models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="parent", related_name='sons', on_delete=models.SET_NULL, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.text}: {self.movie}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='likes')
    
class DisLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='dislikes')

class Reviews(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField( max_length=550)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_movie')
    number = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.movie.title} : {self.number}'
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Forgot_pass(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=25)