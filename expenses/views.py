from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, summary_per_date, expenses_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            if date_from and date_to is None:
                queryset = queryset.filter(date__icontains=date_from)
            if date_to and date_from is None:
                queryset = queryset.filter(date__icontains=date_to)
            if date_from and date_to:
                queryset = queryset.filter(date__range=[date_from, date_to])

            categories = form.cleaned_data.get('categories')
            if categories:
                queryset = queryset.filter(category__in=categories)

            sort = form.cleaned_data.get('algorithm')
            if sort == '1':
                queryset = queryset.order_by('-date')
            if sort == '2':
                queryset = queryset.order_by('date')
            if sort == '3':
                queryset = queryset.order_by('-category')
            if sort == '4':
                queryset = queryset.order_by('category')

        total_amount = sum((obj.amount for obj in queryset))

        return super().get_context_data(
            form=form,
            object_list=queryset,
            total_amount=total_amount,
            summary_per_category=summary_per_category(queryset),
            summary_per_date=summary_per_date(queryset),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        return super().get_context_data(
            object_list=queryset,
            expenses_per_category=expenses_per_category(),
            ** kwargs)
