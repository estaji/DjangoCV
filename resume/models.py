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

class Education(models.Model):
    university = models.CharField(max_length=30)
    level = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)

    def __str__(self):
        return self.level + ' at ' +self.university

class Skill(models.Model):
    STAR_CHOICES = (
        (1, ("1")),
        (2, ("2")),
        (3, ("3")),
    )
    skill = models.CharField(max_length=40)
    star = models.IntegerField(choices=STAR_CHOICES, default=1)

    def __str__(self):
        return self.skill

class Language(models.Model):
    lang = models.CharField(max_length=10)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.lang

class Honor(models.Model):
    honor = models.CharField(max_length=60)
    
    def __str__(self):
        return self.honor