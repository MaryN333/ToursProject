from django.contrib import admin
from .models import Tour, Category, Review

admin.site.site_header = "Tours Admin"
admin.site.site_title = "My Tours"
admin.site.index_title = "Welcome to the Tours admin area"


class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category')

# связь Туров с категорией, в панели админ, для изображения в Категории Туров


class ToursInline(admin.TabularInline):
    model = Tour
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]

    inlines = [ToursInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'id', 'tour')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Review, ReviewAdmin)
