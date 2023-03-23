from django.contrib import admin
from .models import UserCat, UserCategories

# Register your models here.
admin.site.register(UserCat)
admin.site.register(UserCategories)