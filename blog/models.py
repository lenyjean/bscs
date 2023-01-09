from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    status = (
        ("Draft","Draft"),
        ("Publish","Publish")
    )
    category_choices = (
        ("Business", "Business"),
        ("Culture", "Culture"), 
        ("Sport", "Sport"),
        ("Food", "Food"),
        ("Politics", "Politics"),
        ("Celebrity", "Celebrity"),
        ("Startups", "Startups"),
        ("Travel", "Travel"),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=status)
    image = models.ImageField(upload_to='content_images')
    category = models.CharField(max_length=200, choices=category_choices)
    about_blog = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Blog'

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.created_date) 