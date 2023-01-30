from django.db import models
from user.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10000)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100000)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="blog", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    snippet = models.TextField()
    body = RichTextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.blog.title