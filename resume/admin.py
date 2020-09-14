from django.contrib import admin
from .models import Job, Education, Skill, Language, Honor, SoftSkill, Jumbotron, Seo

admin.site.register(Seo)
admin.site.register(Jumbotron)
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(SoftSkill)
admin.site.register(Language)
admin.site.register(Honor)
