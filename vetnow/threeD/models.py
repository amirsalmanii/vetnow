from django.db import models
from django.urls import reverse
from product.models import Product, get_filename_ext


# upload_image_path1 --> uip1
def uip1(instance, file_name):
    """
    get file name from form and give that to get_filename_ext for split name and ext
    then
    change name file with sort numbers like --> 1.jpg --> 2.jpg
    """
    name, ext = get_filename_ext(file_name)
    final_name = f'1{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip2(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'2{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip3(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'3{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip4(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'4{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip5(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'5{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip6(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'6{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip7(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'7{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip8(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'8{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip9(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'9{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip10(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'10{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip11(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'11{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip12(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'12{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip13(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'13{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip14(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'14{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip15(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'15{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip16(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'16{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip17(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'17{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip18(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'18{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip19(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'19{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip20(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'20{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip21(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'21{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip22(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'22{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip23(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'23{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip24(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'24{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip25(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'25{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip26(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'26{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip27(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'27{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip28(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'28{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip29(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'29{ext}'
    return f'threed/{instance.product}/{final_name}'


def uip30(instance, file_name):
    name, ext = get_filename_ext(file_name)
    final_name = f'30{ext}'
    return f'threed/{instance.product}/{final_name}'


class ThreeD(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='three_d')
    created_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to=uip1, null=True, blank=True)
    image2 = models.ImageField(upload_to=uip2, null=True, blank=True)
    image3 = models.ImageField(upload_to=uip3, null=True, blank=True)
    image4 = models.ImageField(upload_to=uip4, null=True, blank=True)
    image5 = models.ImageField(upload_to=uip5, null=True, blank=True)
    image6 = models.ImageField(upload_to=uip6, null=True, blank=True)
    image7 = models.ImageField(upload_to=uip7, null=True, blank=True)
    image8 = models.ImageField(upload_to=uip8, null=True, blank=True)
    image9 = models.ImageField(upload_to=uip9, null=True, blank=True)
    image10 = models.ImageField(upload_to=uip10, null=True, blank=True)
    image11 = models.ImageField(upload_to=uip11, null=True, blank=True)
    image12 = models.ImageField(upload_to=uip12, null=True, blank=True)
    image13 = models.ImageField(upload_to=uip13, null=True, blank=True)
    image14 = models.ImageField(upload_to=uip14, null=True, blank=True)
    image15 = models.ImageField(upload_to=uip15, null=True, blank=True)
    image16 = models.ImageField(upload_to=uip16, null=True, blank=True)
    image17 = models.ImageField(upload_to=uip17, null=True, blank=True)
    image18 = models.ImageField(upload_to=uip18, null=True, blank=True)
    image19 = models.ImageField(upload_to=uip19, null=True, blank=True)
    image20 = models.ImageField(upload_to=uip20, null=True, blank=True)
    image21 = models.ImageField(upload_to=uip21, null=True, blank=True)
    image22 = models.ImageField(upload_to=uip22, null=True, blank=True)
    image23 = models.ImageField(upload_to=uip23, null=True, blank=True)
    image24 = models.ImageField(upload_to=uip24, null=True, blank=True)
    image25 = models.ImageField(upload_to=uip25, null=True, blank=True)
    image26 = models.ImageField(upload_to=uip26, null=True, blank=True)
    image27 = models.ImageField(upload_to=uip27, null=True, blank=True)
    image28 = models.ImageField(upload_to=uip28, null=True, blank=True)
    image29 = models.ImageField(upload_to=uip29, null=True, blank=True)
    image30 = models.ImageField(upload_to=uip30, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('threed:show_3d_images', args=[self.product.slug])
    
    def __str__(self):
        return f'3d for {self.product}'
