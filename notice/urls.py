
from django.contrib import admin
from django.urls import path,include
from note.views import home,validate,home1,additem,update
from .settings import MEDIA_ROOT,MEDIA_URLS
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('note',home1),
    path('validate',validate),
    path('additem',additem),
    path('update/<int:value>',update),
    path('gate/',include('gate.urls'))

]+static(MEDIA_URLS,document_root=MEDIA_ROOT)
