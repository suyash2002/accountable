from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=128)
    body=models.TextField()
    # user = models.ForeignKey(User,
    #                          on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    # upvotes=models.IntegerField()
    # downvotes=models.IntegerField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post')
