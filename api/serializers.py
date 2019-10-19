from rest_framework import serializers

from api.models import Indicator


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Indicator
