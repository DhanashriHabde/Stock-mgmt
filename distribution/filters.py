import django_filters
from .models import DistributeStock
from django_filters import ChoiceFilter
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


section = (
    ('Primary','Primary'),
    ('5th-8th','5th-8th'),
    ('9th-10th','9th-10th'),
    ('Junior college','Junior college'),
)


class StockFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )

    section=ChoiceFilter(choices=section)
  
    class Meta:
        model = DistributeStock
        fields = ['section', 'date', 'stock_name', ]