# movies :
# 1-2-3-4-5-6-7-8-9-10


# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from datetime import datetime, date
# from ckeditor.fields import RichTextField
# from django.utils import timezone


### fdevelop >> models.py


# class Category(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


# class Tag(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


# class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=300, default="Post Title")
    #context = models.TextField()
    context = RichTextField(blank=True, null=True)
    release_datetime = models.DateTimeField(default=timezone.now) 
    image_cover = models.ImageField(null=True, blank=True, upload_to="images/") 
    review = models.TextField(max_length=300, default="sadegh.dev")      
    url = models.SlugField(max_length=300,unique=True,default="aa") 

    def __str__(self):
        return str(self.id) + ' | ' + self.title + ' | ' + str(self.author.first_name) + ' ' + str(self.author.last_name)

    #this is for form in add_fdevelop.html and 
    # bad az zadan dokmeye post, be safheye deail haman post montaghel mishavad.
    def get_absolute_url(self):
        '''way: #1'''
        return reverse('fdevelop')
        '''way: #2 #this have problem for more 10'''
        #return reverse('fdevelop-detail', args=(str(self.id))) 


