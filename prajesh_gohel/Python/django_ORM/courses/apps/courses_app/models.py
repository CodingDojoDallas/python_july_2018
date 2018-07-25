from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Please input a course name!"

        elif len(postData['name']) < 5:
            errors['name'] = "Name needs to be at least 5 characters!"

        if len(postData['desc']) < 1:
            errors['desc'] = "Please input a description for your course!"

        elif len(postData['desc']) < 15:
            errors['desc'] = "Description must be at least 15 characters!"

        return errors

    def comment_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "You need to write a comment!"

        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "<Course object: {} {} {}>".format(self.name, self.desc, self.created_at)

class Comment(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course, related_name = "comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "<Comment object: {}>".format(self.text)
