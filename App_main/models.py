from django.db import models
from App_auth.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    bio = models.TextField()
    social_media_accounts = models.URLField()


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(CustomUser, related_name='liked_posts')
    comments = models.ManyToManyField(CustomUser, through='Comment', related_name='commented_posts')
    shared_by = models.ManyToManyField(CustomUser, related_name='shared_posts')

    def get_comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Connection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_connections')
    connection = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='connections')
    created_at = models.DateTimeField(auto_now_add=True)
