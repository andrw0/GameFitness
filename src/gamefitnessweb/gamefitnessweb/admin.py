from django.contrib import admin
from .models import users,games,exercises
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserForm, UserChangeForm
from .models import users


class CustomUserAdmin(UserAdmin):
    add_form = UserChangeForm
    form = UserForm
    model = users
    list_display = ['username','first_name','last_name','email','height','weight','gender']

admin.site.register(users, CustomUserAdmin)
