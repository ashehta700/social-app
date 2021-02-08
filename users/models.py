from django.db import models
from django.contrib.auth.models import User
#to resize our images that you uploaded it you must use the libaray called Pil that is used for load image field in first
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg' , upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    # use the library to resize your photos that is updated
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def save(self ,*args , **kawrgs):
        super().save(*args , **kawrgs)
        
        img=Image.open(self.image.path)
        
        if img.width > 300 or img.height > 300 :
            out_put = (300,300)
            img.thumbnail(out_put)
            img.save(self.image.path)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\        
             
