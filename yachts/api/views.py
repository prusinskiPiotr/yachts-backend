from ..models import Yacht, Rental
from rest_framework import viewsets, pagination
from .serializer import YachtSerializer, RentalSerializer


class ResultPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'

# ViewSets define the view behavior.
class YachtViewSet(viewsets.ModelViewSet):
    queryset = Yacht.objects.all()
    serializer_class = YachtSerializer
    pagination_class = ResultPagination


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = ResultPagination
