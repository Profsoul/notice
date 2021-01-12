
from django.contrib import admin
from django.urls import path
from note.views import home,validate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('validate',validate)

]
