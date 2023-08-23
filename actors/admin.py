from django.contrib import admin
from .models import Actor
from django.utils.safestring import mark_safe

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','name','main_site','formatted_hit_count','get_image','is_active')
    list_display_links = ('id','name')
    list_editable = ('is_active',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90", height="100"')
    
    get_image.short_description = 'Изображение'

    def formatted_hit_count(self, obj):
        return obj.current_hitcount() if obj.current_hitcount() >0 else '-'
    formatted_hit_count.short_description = 'Просмотры'

admin.site.register(Actor,ActorAdmin)