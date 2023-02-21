from django.contrib import admin
from apps.users.models import *
# Register your models here.
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user','movie', 'parent','id')
    list_display_links = ('movie',)
    readonly_fields = ('user',)


admin.site.register(User)
