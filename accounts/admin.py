from django.contrib import admin
from accounts.models import User, Admin

# Register your models here.
admin.site.register(User, Admin)
