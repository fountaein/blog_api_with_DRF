from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

class Category(models.Model):
   title = models.CharField(max_length=100)

   def __str__(self):        
        return self.title

class Post(models.Model):    
    STATUS_CHOICES = (        
        ('draft', 'Draft'),       
         ('published', 'Published'),   
          )    
    title = models.CharField(max_length=250)    
    slug = models.SlugField(max_length=250,null=False, unique=True)    
    author = models.ForeignKey(User,on_delete=models.CASCADE)    
    body = models.TextField()    
    publish = models.DateTimeField(default=timezone.now)    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)    
    
    class Meta:        
        ordering = ('-publish',)   
        
    def __str__(self):        
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('post_detail', kwargs=kwargs)




    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)






   
