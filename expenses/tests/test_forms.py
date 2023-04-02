import datetime

from django.test import TestCase
from ..models import Category
from ..forms import ExpenseSearchForm


class TestExpenseSearchForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        for category_id in range(4):
            Category.objects.create(name=f'test {category_id}')

    def test_empty_form(self):
        form = ExpenseSearchForm()
        self.assertInHTML('<input type="text" name="name" maxlength="50" id="id_name">', str(form))
        self.assertInHTML('<label for="id_categories">Categories:</label>', str(form))

    def test_date_from_label(self):
        form = ExpenseSearchForm()
        self.assertTrue(form.fields['date_from'].label is None)

    def test_algorithm_label(self):
        form = ExpenseSearchForm()
        self.assertTrue(form.fields['algorithm'].label == 'Select algorithm')

    def test_date_from_field(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = ExpenseSearchForm(data={'date_from': date})
        self.assertTrue(form.is_valid())

    def test_categories_field(self):
        for category in Category.objects.all():
            form = ExpenseSearchForm(data={'categories': [f'{category.id}']})
            self.assertTrue(form.is_valid())
