from django.contrib import admin
from .models import Posts
# Register your models here.


# allow the Posts table to show on the admin page
admin.site.register(Posts)