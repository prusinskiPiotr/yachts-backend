from rest_framework import serializers
from ..models import Yacht, Rental

# Serializers define the API representation.
class YachtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yacht
        fields = ['model_name', 'length', 'width', 'year', 'max_crew', 'berths', 'owner']


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'from_date', 'to_date', 'insurance', 'yacht', 'user']
