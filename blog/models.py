from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse # after submitting reverse redirects user back to where they came from 

# Create your models here. (classes)

class Posts (models.Model ):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)      # import user class
    title = models.CharField(max_length=100)                        # max 100 chars for title
    content = models.TextField()                                    # big string
    date_posted = models.DateTimeField(default=timezone.now)        # on blog creation date
    last_modified = models.DateTimeField(auto_now=True)             # everytime blog is updated
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})   # the instance of post pk
    
    