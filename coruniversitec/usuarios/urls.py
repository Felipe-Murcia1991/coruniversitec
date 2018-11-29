from django.conf.urls import url
from usuarios.views import Bienvenidos



urlpatterns=[
    url(
        regex=r'^Bienvenidos/$',
        view=Bienvenidos,
        name='Bienvenidos_a _SDAF',
    )

]
