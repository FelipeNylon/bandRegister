
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from bandsmanage.api import viewsets as BandsmanageViewset


route = routers.DefaultRouter()

route.register(r'bands', BandsmanageViewset.BandsmanageViewset, basename="bands")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
