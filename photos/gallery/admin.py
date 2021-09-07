from django.contrib import admin
from .models import Location, Category, Image


# Register your models here.

admin.site.register(Location)
admin.site.register(Category)


class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display       = ['image_name', 'location', 'category', 'active', 'pub_date']
    list_display_links = ['image_name']
    list_filter   = ['location', 'category', 'active']
    search_fields = ['location__location', 'category__category']
    readonly_fields = ['pub_date']
    list_per_page = 25
    class Meta:
        model = Image
admin.site.register(Image, ImageAdmin)


