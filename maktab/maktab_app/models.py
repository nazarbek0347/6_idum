from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="media", blank=False)
    tglink = models.URLField(default="http://example.com",blank=False)

    def __str__(self):
        return self.title
    