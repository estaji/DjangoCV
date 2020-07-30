from django.contrib import admin
from .models import Job, Education, Skill, Language, Honor, SoftSkill

admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(SoftSkill)
admin.site.register(Language)
admin.site.register(Honor)