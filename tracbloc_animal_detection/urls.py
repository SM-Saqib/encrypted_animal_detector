"""tracbloc_animal_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.contrib import admin

# from django.urls import include, path
from django.urls import include, path, re_path


# urlpatterns = [

#     path('animal_detector_app/', include('animal_detector_app.urls')),
#     path('admin/',admin.site.urls),
# ]

from django.apps import apps
import animal_detector_app.urls

urlpatterns = [
    path(r"^admin/", admin.site.urls),
]

app_name = apps.get_app_config("animal_detector_app").name
urlpatterns += [
    path("", include((animal_detector_app.urls, app_name), namespace=app_name)),
]
