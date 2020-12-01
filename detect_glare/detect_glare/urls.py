from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from sunglare.views import glareView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', glareView.as_view(), name='detect_glare')
]
