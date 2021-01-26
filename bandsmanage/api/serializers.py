from rest_framework import serializers
from bandsmanage import models

class BandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bands
        fields = '__all__'