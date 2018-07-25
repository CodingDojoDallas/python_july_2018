from __future__ import unicode_literals
from django.db import models

class JobManager(models.Manager):
    def job_validation(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "You must input a title!"

        elif len(postData['title']) < 4:
            errors['title'] = "Title must be at least four characters!"

        if len(postData['desc']) < 1:
            errors['desc'] = "You must input a description!"

        elif len(postData['desc']) < 11:
            errors['desc'] = "Description must be at least ten characters!"

        if len(postData['location']) < 1:
            errors['location'] = "You must input a location!"

        return errors

class Job(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    location = models.CharField(max_length = 255)
    user = models.ForeignKey('login.User', related_name = 'jobs', on_delete = models.CASCADE)
    user_jobs = models.ManyToManyField('login.User', related_name = 'jobs_for_user')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = JobManager()
    def __repr__(self):
        return "<Job object: {} {} {}>".format(self.title, self.desc, self.location)
