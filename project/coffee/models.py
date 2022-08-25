from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50)
    material = models.ManyToManyField('Material')
    image = models.ImageField('IMAGE', upload_to='coffee/%Y/%m', blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    bookmark = models.ManyToManyField(get_user_model(), blank=True)
    
    class Meta:
        ordering = ('update_dt',)
        
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    