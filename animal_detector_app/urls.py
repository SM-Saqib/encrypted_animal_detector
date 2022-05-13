# from django.urls import path
# from . import views
# urlpatterns= [
#     path("",views.index,name="index"),
# ]

from django.conf.urls import url
from animal_detector_app.views import user_list

url_pattern = [
    url(r'^$',user_list, name= 'user_list'),
]