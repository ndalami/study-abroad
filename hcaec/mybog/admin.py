from django.contrib import admin
from . models import Clients, Post, Student,University

# Register your models here.
admin.site.register(Clients)
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(University)
admin.site.site_header = 'HCAEC ADMINISTRATION'

