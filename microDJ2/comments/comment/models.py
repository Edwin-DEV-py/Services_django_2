from django.db import models

class Comment(models.Model):
    postID = models.IntegerField()
    content = models.TextField(max_length=300)