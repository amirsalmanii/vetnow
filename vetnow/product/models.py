import os
from datetime import date
from datetime import datetime
from io import BytesIO
from random import randrange

from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from .managers import ProductExistManager

User = settings.AUTH_USER_MODEL
THUMB_SIZE = (400, 400)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:category_products', args=[self.slug])


def get_filename_ext(FilePath):
    """
    this function get file path of images and thumbnail and split base filepath and ext
    like:
    iphone12.jpg --> iphone12 | jpg
    """
    base_name = os.path.basename(FilePath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# This datas is for the bottom two functions
def give_data_to_path():
    new_name = randrange(1000, 9999)
    data_now = str(date.today())
    split_date = datetime.strptime(data_now, "%Y-%m-%d")
    return new_name, data_now, split_date


def upload_image_path(instance, file_name):
    """
    get file name from form and give that to get_filename_ext for split name and ext
    then
    change name file with random numbers like --> you.jpg --> 22.jpg
    and save in return path with split dates like --> 2021/12/filename.
    """
    new_name, data_now, split_date = give_data_to_path()
    y, m = split_date.year, split_date.month
    name, ext = get_filename_ext(file_name)
    final_name = f'{new_name}{ext}'
    return f'images/products/{y}/{m}/{final_name}'


def upload_thumbnail_path(instance, file_name):
    """
    get file name from form and give that to get_filename_ext for split name and ext
    then
    change name file with random numbers like --> you.jpg --> 22.jpg
    and save in return path with split dates like --> 2021/12/filename.
    """
    new_name, data_now, split_date = give_data_to_path()
    y, m = split_date.year, split_date.month
    name, ext = get_filename_ext(file_name)
    final_name = f'{new_name}{ext}'
    return f'thumbnails/products/{y}/{m}/{final_name}'


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, allow_unicode=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=upload_thumbnail_path, blank=True, null=True)
    pdf_file = models.FileField(upload_to='products/pdfs/', null=True, blank=True)
    descreption = RichTextUploadingField(null=True, blank=True)
    available = models.BooleanField(default=True)
    price = models.BigIntegerField(default=0)
    company_price = models.BigIntegerField(default=0)
    manufacturer_company = models.CharField(max_length=120, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=0)
    like_count = models.BigIntegerField(default=0, null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    objects = ProductExistManager()

    def __str__(self):
        return self.name

    # make thumbnail from original image and save it.
    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            pass

        if self.quantity == 0:
            self.available = False
        elif self.quantity >= 1:
            self.available = True

        self.slug = self.name.replace(' ', '-')
        super(Product, self).save(*args, **kwargs)

    def make_thumbnail(self):
        # if user set image
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

            thumb_name, thumb_extension = os.path.splitext(self.image.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + '_thumb' + thumb_extension

            if thumb_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif thumb_extension == '.gif':
                FTYPE = 'GIF'
            elif thumb_extension == '.png':
                FTYPE = 'PNG'
            else:
                return False  # Unrecognized file type

            # Save thumbnail to in-memory file as StringIO
            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            # set save=False, otherwise it will run in an infinite loop
            self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
            temp_thumb.close()

            return True
        else:
            return ''

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])


class LikeProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likesp')
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} liked {self.product.name}'


@receiver(post_save, sender=LikeProduct)
def product_liked_count_update(sender, instance, **kwargs):
    product = instance.product
    if not instance.liked:
        product.like_count += 1
        product.save()
        instance.liked = True
        instance.save()
    else:
        pass
