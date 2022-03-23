
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from .models import *
from .forms import *

# Register your models here.

# Custom Accounts
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "id",
        "email",
        "user_nicename",
        "user_registered",
        "is_staff",
        "password",
    )
    list_filter = (
        "email",
        
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("user_login", "password", "email", "displayname")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user_login",
                    "displayname",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("user_login",)
    ordering = ("id",)


admin.site.register(CustomUser, CustomUserAdmin)

