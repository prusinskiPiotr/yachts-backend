from rest_framework import viewsets, pagination, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import YachtSerializer, RentalSerializer

from ..models import Yacht, Rental


class ResultPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'

# ViewSets define the view behavior.
class YachtViewSet(viewsets.ModelViewSet):
    queryset = Yacht.objects.all()
    serializer_class = YachtSerializer
    pagination_class = ResultPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['model_name', 'length', 'width', 'year', 'max_crew', 'berths']
    search_fields = ['model_name', 'year']


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = ResultPagination
