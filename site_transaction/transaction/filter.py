from django_filters import rest_framework as rf
from .models import *


class Filter(rf.FilterSet):
#    date_max = rf.DateFilter(field_name='time', lookup_expr='lt')
#    date_min = rf.DateFilter(field_name='time', lookup_expr='qt')
    date = rf.DateFromToRangeFilter(field_name='date')
    time = rf.TimeRangeFilter(field_name='time')
    summ_min = rf.NumberFilter(field_name="summ", lookup_expr='gt')
    summ_max = rf.NumberFilter(field_name="summ", lookup_expr='lt')
    class Meta:
        model = TransactionsUser
        fields = ['summ', 'time', 'date']