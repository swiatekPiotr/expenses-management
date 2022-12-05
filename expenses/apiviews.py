from rest_framework import viewsets

from .models import Expense
from .serializers import ExpenseSerializer


class ExpensesApi(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer
