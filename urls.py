from django.conf.urls import url
from LX import views
urlpatterns=[
    url(r'^getgrades',views.getgrades),
]
