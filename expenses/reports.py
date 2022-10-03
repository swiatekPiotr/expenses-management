from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def summary_per_date(queryset):
    return OrderedDict(sorted(
        queryset
        .order_by()
        .values('date__year')
        .annotate(s=Sum('amount'))
        .values_list('date__year', 's')
    ))
