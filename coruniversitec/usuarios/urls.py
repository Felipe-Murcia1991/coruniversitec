from django.conf.urls import url
from . import views



urlpatterns=[
    url(
        regex=r'^Bienvenidos/$',
        view=views.Bienvenidos,
        name='Bienvenidos_a _SDAF',
    )

]
