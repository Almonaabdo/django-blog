from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile (models.Model):
     # one-to-one relationship (Cascare allows to if a user is deleted, delete its profile but not the opposite)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    
    
    
    def __str__(self):
        
        return f'{self.user.username} Profile'
    
    
    # overridding save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)    # running the parent save method
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            
            #override image size if its big
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

    