from django.contrib import admin
from poll.models import Poll, Option, Comment

# Register your models here.
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Comment)