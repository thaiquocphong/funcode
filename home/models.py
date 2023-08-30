from django.db import models
from tinymce.models import HTMLField
from .custom_field import *
import uuid
import os

# Create your models here.

class Category(models.Model):
    LAYOUT_CHOICE =(
        ('list', 'List'),
        ('grid', 'Grid')
    )
    STATUS_CHOICE =(
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICE, default='list')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self) -> str:
        return self.name
    
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/article/', filename)

class Article(models.Model):
    STATUS_CHOICE =(
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Article"

    def __str__(self) -> str:
        return self.name
    

class Feed(models.Model):
    STATUS_CHOICE =(
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Feed"

    def __str__(self) -> str:
        return self.name

