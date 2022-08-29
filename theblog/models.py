from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home" )

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="My Blog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)

    post_date = models.DateField(auto_now_add=True)
    Category = models.CharField(max_length=255, default='uncategorized')
    snippet = models.CharField(max_length=255, default='Click link above to read the blog post.....')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' +str(self.author)

    def get_absolute_url(self):
        return reverse("home" )


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='user_releted_profile')
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    twitter_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True, max_length=255)
    linkdin_url = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home" )

class Contact(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("home" )
