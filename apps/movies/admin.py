from django.contrib import admin
from apps.movies.models import *
from apps.users.models import Reviews
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name',)
    prepopulated_fields = {'slug' : ('name', )}
    
class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('user',)

class PhotomovieInline(admin.TabularInline):
    list_display = ('id', 'movie',)
    model = Photomovie
    extra = 1
    readonly_fields = ('get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="100" height="100">')
    
    get_image.short_description = "Изображение"
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','slug', 'get_poster',)
    list_filter = ('category','year')
    search_fields = ('title', 'category__name')
    list_display_links = ('id', 'title','get_poster',)
    prepopulated_fields = {'slug' : ('title', )}
    inlines =[ PhotomovieInline,ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_poster',)
    
    def get_poster(self, obj):
        return mark_safe(f'<img src = {obj.poster.url} width="100" height="100">')
    
    get_poster.short_description = "Изображение"
    
@admin.register(Photomovie)
class PhotomovieAdmin(admin.ModelAdmin):
    list_display = ('movie','get_image',)
    readonly_fields = ('get_image',)
    list_display_links = ('movie','get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="100" height="100">')
    
    get_image.short_description = "Галерея"
    
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('series','get_image',)
    list_display_links = ('series','get_image',)
    
    def get_image(self, obj):   
        return mark_safe(f'<img src = {obj.series.poster.url} width="100" height="100">')
    
    get_image.short_description = "Серии"