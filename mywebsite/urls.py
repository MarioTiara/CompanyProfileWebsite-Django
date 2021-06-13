from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/',include("about.urls")),
    url(r'^service/',include('service.urls')),
    url(r'^product/',include('product.urls')),
    url(r'^portofolio/',include('portofolio.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^$',views.index),
]
