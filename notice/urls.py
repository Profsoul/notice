
from django.contrib import admin
from django.urls import path
from note.views import home,validate,home1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('note',home1),
    path('validate',validate)

]
