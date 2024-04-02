from django.contrib import admin

# Register your models here.
from .models import Demo, Role, CustomUser
admin.site.register(Demo)
admin.site.register(Role)
admin.site.register(CustomUser)



