from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)

    # ✅ Cloudinary image field
    image = CloudinaryField('image', blank=True, null=True)

    content = models.TextField(max_length=100000)

    # ✅ Automatically store creation time
    time = models.DateTimeField(auto_now_add=True)

    likes = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.postname}"


class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.id} | {self.content[:30]}"


class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject[:30]}"
