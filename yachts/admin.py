from django.contrib import admin
from .models import Yachts, Rentals


@admin.register(Yachts)
class YachtsAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'length', 'width', 'year', 'max_crew', 'berths', 'owner')


@admin.register(Rentals)
class RentalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_date', 'to_date', 'insurance', 'yacht', 'user')

