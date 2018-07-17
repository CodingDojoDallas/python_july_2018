from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "You must input a first name!"

        elif not postData['first_name'].isalpha():
            errors['first_name'] = "Please use letters for your name only"

        if len(postData['last_name']) < 1:
            errors['last_name'] = "You must input a last name!"

        elif not postData['last_name'].isalpha():
            errors['last_name'] = "Please use letters for your name only"

        if len(postData['email']) < 1:
            errors['email'] = "Please input an email address!"

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Dojo object: {} {} {}>".format(self.first_name, self.last_name, self.email)
