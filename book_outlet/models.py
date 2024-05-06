from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# from django.core.urlresolvers import reverse
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, default='Unknown')
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True) 

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save()

    def __str__(self):
        return f"{self.title}({self.rating})"