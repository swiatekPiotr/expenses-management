from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from .models import Expense, Category
from .views import ExpenseListView, CategoryListView
from .apiviews import ExpensesApiList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/', ExpensesApiList.as_view(), name='expense-api-list'),

    path('expense/list/',
         ExpenseListView.as_view(),
         name='expense-list'),
    path('expense/create/',
         CreateView.as_view(
            model=Expense,
            fields='__all__',
            success_url=reverse_lazy('expenses:expense-list'),
            template_name='generic_update.html'
         ),
         name='expense-create'),
    path('expense/<int:pk>/edit/',
         UpdateView.as_view(
            model=Expense,
            fields='__all__',
            success_url=reverse_lazy('expenses:expense-list'),
            template_name='generic_update.html'
         ),
         name='expense-edit'),
    path('expense/<int:pk>/delete/',
         DeleteView.as_view(
            model=Expense,
            success_url=reverse_lazy('expenses:expense-list'),
            template_name='generic_delete.html'
         ),
         name='expense-delete'),

    path('category/list/',
         CategoryListView.as_view(),
         name='category-list'),
    path('category/create/',
         CreateView.as_view(
            model=Category,
            fields='__all__',
            success_url=reverse_lazy('expenses:category-list'),
            template_name='generic_update.html'
         ),
         name='category-create'),
    path('category/<int:pk>/edit/',
         UpdateView.as_view(
            model=Category,
            fields='__all__',
            success_url=reverse_lazy('expenses:category-list'),
            template_name='generic_update.html'
         ),
         name='category-edit'),
    path('category/<int:pk>/delete/',
         DeleteView.as_view(
            model=Category,
            success_url=reverse_lazy('expenses:category-list'),
            template_name='generic_delete.html'
         ),
         name='category-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
