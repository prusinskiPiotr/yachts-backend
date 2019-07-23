from django.contrib import admin
from .models import Yacht, Rental


@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'length', 'width', 'year', 'max_crew', 'berths', 'owner')


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_date', 'to_date', 'insurance', 'yacht', 'user')

