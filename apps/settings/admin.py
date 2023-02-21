from django.contrib import admin
from apps.settings.models import Settings, Privacy, About, Media,Partners, PartnersImage, Contact
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.register(Settings)
admin.site.register(Privacy)
admin.site.register(Partners)
admin.site.register(PartnersImage)
admin.site.register(About)
admin.site.register(Contact)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('about','get_image',)
    readonly_fields = ('get_image',)
    list_display_links = ('about','get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="100" height="100">')
    
    get_image.short_description = "Галерея"
    

