from django.contrib import admin
from .models import Services, Category, GetIntouch


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')


admin.site.register(Services, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GetIntouch, GetInTouchAdmin)