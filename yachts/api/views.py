from ..models import Yacht, Rental
from rest_framework import viewsets
from .serializer import YachtSerializer, RentalSerializer


# ViewSets define the view behavior.
class YachtViewSet(viewsets.ModelViewSet):
    queryset = Yacht.objects.all()
    serializer_class = YachtSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
