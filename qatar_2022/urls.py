from django.contrib import admin
from django.urls import path, include
from qatar_2022.views import index,about

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('products/',include('products.urls')),
    path('news/',include('news.urls')),
    path('win/',include('win.urls')),
    path('users/',include('users.urls')),
    path('about/',about,name='about'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)