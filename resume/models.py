from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logos/')
    company = models.CharField(max_length=30)
    url = models.URLField(max_length=20, default='http://#')
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title + ' at ' +self.company