from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=150, null=False)
    excerpt = models.CharField(max_length=200, null=False)
    image = models.CharField(max_length=200, null=False)
    data = models.DateField(null=False, auto_now=True)
    slug = models.SlugField(unique=True, default='', null=False)
    content = models.TextField(null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,null=True, related_name='post')
    tag = models.ManyToManyField(Tag,)
