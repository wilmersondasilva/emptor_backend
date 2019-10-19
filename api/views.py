from rest_framework import viewsets, mixins

from api.serializers import IndicatorSerializer
from api.models import Indicator


class IndicatorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = IndicatorSerializer
    queryset = Indicator.objects.all()
