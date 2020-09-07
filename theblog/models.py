from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    header_image=models.ImageField(null=True, blank=True, upload_to="images/" )
    updated_on = models.DateTimeField(auto_now= True)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name ='blog_posts')
    #status = models.IntegerField(choices=STATUS, default=0)

    #class Meta:
     #s   ordering = ['-created_on']
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

