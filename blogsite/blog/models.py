from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
