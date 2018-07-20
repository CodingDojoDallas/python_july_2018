from __future__ import unicode_literals
from django.db import models
from datetime import date
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        result = User.objects.filter(email=postData['email'])
        today = date.today()
        born = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d")
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if len(postData['first_name']) < 1:
            errors['first_name'] = "You must input a first name!"

        elif len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than two characters!"

        elif not postData['first_name'].isalpha():
            errors['first_name'] = "Please use letters for your name only"

        if len(postData['last_name']) < 1:
            errors['last_name'] = "You must input a last name!"

        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be more than two characters!"

        elif not postData['last_name'].isalpha():
            errors['last_name'] = "Please use letters for your name only"

        if age < 13:
            errors['birthday'] = "You must be 13 years or older to register!"

        if len(postData['email']) < 1:
            errors['email'] = "Please input an email address!"

        elif len(result) != 0:
            errors['email'] = "This email has already been taken!!!!"

        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Needs a valid email address!"

        if len(postData['password']) < 1:
            errors['password'] = "Please input a password!"

        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long!"

        if len(postData['pass_confirm']) < 1:
            errors['pass_confirm'] = "Please confirm your password!"

        elif postData['password'] != postData['pass_confirm']:
            errors['pass_confirm'] = "Passwords must match!"

        return errors

    def login_validator(self, postData):
        errors = {}
        result = User.objects.filter(email=postData['email'])
        if len(postData['email']) < 1:
            errors['email'] = "Please input your email address!"

        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Needs a valid email address!"

        elif len(result) == 0:
            errors['email'] = "Login failed"

        if len(postData['passlog']) < 1:
            errors['passlog'] = "Please input a password!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    birthday = models.DateField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.birthday)

class Message(models.Model):
    user = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Message object: {}>".format(self.message)

class Comment(models.Model):
    comment = models.TextField()
    user_comment = models.ForeignKey(User, related_name = "comments_from_user", on_delete = models.CASCADE)
    message_comment = models.ForeignKey(Message, related_name = "comments_in_message", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Comment object: {}>".format(self.comment)
