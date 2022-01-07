from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, null=True, blank=True)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
