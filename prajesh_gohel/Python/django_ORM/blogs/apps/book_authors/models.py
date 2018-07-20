from __future__ import unicode_literals
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Dojo object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    authors = models.ManyToManyField(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Dojo object: {} {}>".format(self.name, self.desc)
