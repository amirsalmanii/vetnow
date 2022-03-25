from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.admin import (
    TokenProxy,
    TokenAdmin,
)  # edit for unregister in admin
from .models import User as CustomUser, IpTables
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    form_add = UserCreationForm
    list_display = (
        "username",
        "first_name",
        "user_image",
        "last_name",
        "is_admin",
        "is_doctor",
    )
    list_filter = ("is_admin", "is_doctor")
    search_fields = ("email", "username")
    list_editable = ("is_doctor",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "national_code",
                    "national_code_image",
                    "Incubation_license",
                    "other",
                    "job",
                    "graduate",
                    "experience",
                    "doctorDescreption",
                    "doctorId",
                    "avatar",
                    "password",
                    "state",
                    "city",
                    "address",
                    "plate",
                    "zip_code",
                    "full_name",
                    "phone_number",
                    "wallet",
                )
            },
        ),
        ("Personal Info", {"fields": ("is_active", "is_doctor")}),
        ("Personal Perms", {"fields": ("is_admin",)}),
    )

    add_fieldsets = ((None, {"fields": ("username", "password1", "password2")}),)

    ordering = ("-id",)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
admin.site.site_header = "vet now"
admin.site.register(IpTables)
