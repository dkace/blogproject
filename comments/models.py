# -*- coding: utf-8 -*-
from django.db import models

class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post',on_delete='')

    def __str__(self):
        return self.text[:20]