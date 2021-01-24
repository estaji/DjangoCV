from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logos/')
    company = models.CharField(max_length=30)
    url = models.URLField(max_length=20, default='http://#')
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    summary = models.TextField()

    def __str__(self):
        return self.title + ' at ' + self.company

    # show last one on top of others
    class Meta:
        ordering = ['-id',]

class Education(models.Model):
    university = models.CharField(max_length=30)
    level = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)

    def __str__(self):
        return self.level + ' at ' + self.university


class Skill(models.Model):
    STAR_CHOICES = (
        (1, ("1")),
        (2, ("2")),
        (3, ("3")),
    )
    skill = models.CharField(max_length=100)
    star = models.IntegerField(choices=STAR_CHOICES, default=1)

    def __str__(self):
        return self.skill


class Language(models.Model):
    lang = models.CharField(max_length=25)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.lang


class Honor(models.Model):
    honor = models.CharField(max_length=60)

    def __str__(self):
        return self.honor


class SoftSkill(models.Model):
    skill = models.CharField(max_length=40)

    def __str__(self):
        return self.skill


class Jumbotron(models.Model):
    greeting = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    text = models.TextField()
    email = models.EmailField(max_length=254)


class Seo(models.Model):
    description = models.CharField(max_length=160)
    author = models.CharField(max_length=50)
    keywords = models.CharField(max_length=100)
    title = models.CharField(max_length=60)


class Bar(models.Model):
    brand = models.CharField(max_length=50)
    linkedin = models.URLField(max_length=200, default="#", blank=True)
    github = models.URLField(max_length=200, default="#", blank=True)
    stackexchange = models.URLField(max_length=254, default="#", blank=True)
    instagram = models.URLField(max_length=200, default="#", blank=True)
    twitter = models.URLField(max_length=200, default="#", blank=True)
