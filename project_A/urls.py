#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
   # path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cities.urls')), # new
]
