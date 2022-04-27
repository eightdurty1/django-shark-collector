from django.contrib import admin

# Register your models here.
from .models import Shark, Feeding
admin.site.register(Shark)
admin.site.register(Feeding)