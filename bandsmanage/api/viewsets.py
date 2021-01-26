from rest_framework import viewsets
from bandsmanage.api import serializers
from bandsmanage import models

class BandsmanageViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BandsSerializer
    queryset = models.Bands.objects.all()