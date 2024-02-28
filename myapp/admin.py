from django.contrib import admin

from .product import Products
from .category import Category

class  categoryinfo(admin.ModelAdmin):
    list_display = ["name"]

class productinfo(admin.ModelAdmin):
    list1_display = ["name","category"]


admin.site.register(Category,categoryinfo)
admin.site.register(Products,productinfo)


# Register your models here.
