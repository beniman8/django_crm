from django.contrib import admin
from .models import User,Lead,Agent,UserProfile,Category
# Register your models here.

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Category)