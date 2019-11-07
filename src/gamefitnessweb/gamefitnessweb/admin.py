from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import users,games,exercises

admin.site.register(users)
