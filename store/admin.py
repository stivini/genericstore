from django.contrib import admin
from .models import Users, Products, Category, DefaultImages

admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(DefaultImages)
