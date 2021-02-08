from PIL import Image
from django.db import models
from django.utils import timezone
# import table in user in admin panel
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    data_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="post_photo")
    video = models.FileField(upload_to='post_videos')
    
    
    def __str__(self):
        return self.title 
    # this for get url after submit the new Post !
    def get_absolute_url(self):
        return reverse('blog-home')