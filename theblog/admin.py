from django.contrib import admin
from .models import Post, Category, Profile, Contact

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Contact)
