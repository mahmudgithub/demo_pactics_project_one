#from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "gender", "age",)



admin.site.register(City, CityAdmin,)
