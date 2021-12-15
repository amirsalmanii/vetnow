from django.contrib import admin
from django.contrib.admin import display

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "get_user_first_name", "get_user_last_name", "body", "get_comment_parent", "approved")
    list_editable = ("approved",)
    list_filter = ("created_at", "approved")
    search_fields = ("user__username", "body", "user__first_name", "user__last_name")
    fields = ("user", "product", "parent", "body")

    @display(ordering='', description='First name')
    def get_user_first_name(self, obj):
        return obj.user.first_name

    @display(ordering='', description='Last name')
    def get_user_last_name(self, obj):
        return obj.user.last_name

    @display(ordering='', description='To')
    def get_comment_parent(self, obj):
        return obj.parent

    class Meta:
        ordering = ("created_at",)
