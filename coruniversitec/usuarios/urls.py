from django.conf.urls import url
from . import views



urlpatterns=[
    url(
        path('', views.Bienvenidos, name='Bienvenidos'),
    )

]
