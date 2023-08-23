from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('author',)

class FilmAdmin(admin.ModelAdmin):
    list_display = ('id','title','studio','rating_IMDb','formatted_hit_count','get_image','is_active')
    list_display_links = ('id','title')
    list_editable = ('rating_IMDb','is_active','studio')
    list_filter = ('release_date','is_active','studio')
    search_fields = ('title','desc')
    inlines = [ReviewInLine]
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90", height="100"')
    
    get_image.short_description = 'Изображение'

    def formatted_hit_count(self, obj):
        return obj.current_hitcount() if obj.current_hitcount() > 0 else '-'

    formatted_hit_count.short_description = 'Просмотры'

admin.site.register(Film, FilmAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','film','author','comment','rating','get_like_dislike_count')
    list_display_links = ('id','film')
    def get_like_dislike_count(self, obj):
        lcount = ReviewLike.objects.filter(review_id = obj.pk, value = 1).count()
        dlcount = ReviewLike.objects.filter(review_id = obj.pk, value = 0).count()
        if lcount==0:
            lcount = '-'
        if dlcount==0:
            dlcount = '-'
        return f'{lcount} | {dlcount}'
    get_like_dislike_count.short_description = 'Likes/Dislikes'

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewLike)
admin.site.register(Genre)

admin.site.site_title = 'Django Films'
admin.site.site_header = 'Django Films'