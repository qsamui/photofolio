from django.db import models
from django.urls import reverse

class Photographer(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    portrait = models.ImageField(upload_to='portrait/')
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    def __str__(self): return self.name 

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='categories/')
    price_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('category_detail', args=[self.slug])

class SessionImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='sessions/')
    caption = models.CharField(max_length=200, blank=True)
    def __str__(self): 
        return f"{self.category.name} - {self.caption or self.image.name}"
    

