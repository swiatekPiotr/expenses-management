from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer


class ExpensesApiList(APIView):
    def get(self, request):
        queryset = Expense.objects.all().order_by('-date')
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data)
