from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

User = settings.AUTH_USER_MODEL


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, allow_unicode=True, null=True, blank=True)
    title_image = models.ImageField(upload_to='news/%Y/%m/', null=True, blank=True)
    body = RichTextUploadingField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        # if not self.author:
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
