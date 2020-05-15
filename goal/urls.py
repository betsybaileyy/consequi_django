from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goals/', include('goals.urls')),
    path('admin/', admin.site.urls),
]