from __future__ import unicode_literals
from django.db import models

class QuoteManager(models.Manager):
    def simple_validator(self, postData):
        errors = {}
        if len(postData['author']) < 1:
            errors['author'] = "Please input an author!"

        if len(postData['quote']) < 1:
            errors['quote'] = "You must input a quote, silly!"

        return errors

class Quote(models.Model):
    author = models.CharField(max_length = 255)
    quote = models.TextField()
    user = models.ForeignKey('users.User', related_name = "quotes", on_delete = models.CASCADE)
    user_likes = models.ManyToManyField('users.User', related_name = "quote_likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    def __repr__(self):
        return "<Quote object: {}>".format(self.quote)
