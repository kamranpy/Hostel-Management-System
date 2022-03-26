import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = HostelApply
        fields = ('hostel',
                  'rooms',
                  'app_status',
                  'date_due')