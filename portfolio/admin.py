from django.contrib import admin
from .models import Category, SessionImage, Photographer


@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class SessionImageInline(admin.TabularInline):
    model = SessionImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price_from')
    inlines = [SessionImageInline]

