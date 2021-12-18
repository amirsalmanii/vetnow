import os

from django.conf import settings
from django.db import models
from django.urls import reverse

from product.models import Product, get_filename_ext

# for using in file names like --> 1.jpg, 2.jpg .... 30.jpg
numbers_for_files_name = list(range(1, 31))


def upload_image_path(instance, file_name):
    """
    base --> for get dir images save and return what in this dir(
    if it doesn't have anything we start file name from 1 and to 31
    if you have anything like 1 and 2 and 3 we start fom 4
    )
    """
    base = settings.BASE_DIR / 'media' / 'threed' / f'{instance.product}'
    name, ext = get_filename_ext(file_name)  # for split name of file and ext --> as.jpg --> as and jpg
    number = 1  # default file name when dir base in empty
    try:
        # try to get files list in dir and split that from number and ext and sorted numbers
        # like this --> (2, 3 , 1) --> (1, 2 , 3 ,4)
        list_of_images = os.listdir(base)
        normalize_list_images = []
        for image in list_of_images:
            number, ex = image.split('.')
            normalize_list_images.append(int(number))
        normalize_list_images = sorted(normalize_list_images)
    except:
        # if we can't recognize dir we can say we don't have any file, so we start from 1
        number = 1
    else:
        # when we dont have except
        # we're looping in number and if number not in normalize_list_images we set that for file name
        for n in numbers_for_files_name:
            if n in normalize_list_images:
                pass
            else:
                number = n
                break
    final_name = f'{number}{ext}'
    return f'threed/{instance.product}/{final_name}'


class ThreeD(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='three_d')
    created_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image5 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image6 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image7 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image8 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image9 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image10 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image11 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image12 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image13 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image14 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image15 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image17 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image16 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image18 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image19 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image20 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image21 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image22 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image23 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image24 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image25 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image26 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image27 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image28 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image29 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image30 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('threed:show_3d_images', args=[self.product.slug])
