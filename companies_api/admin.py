from django.contrib import admin

# Register your models here.
from .models import Company, Location 
admin.site.register(Company)
admin.site.register(Location)