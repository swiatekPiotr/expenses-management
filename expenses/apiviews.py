from rest_framework import viewsets

from .models import Expense
from .serializers import ExpenseSerializer


class ExpensesApi(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> instance detail
    post -> create -> new instance
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer
