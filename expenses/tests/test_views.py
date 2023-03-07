from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Expense


class TestExpenseListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for expense_id in range(8):
            Expense.objects.create(name='test {expense_id}', amount=8.88)

    def set_up(self):
        self.client = Client()

    def test_url_exist(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('expenses:expense-list'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertTemplateUsed(response, 'expenses/expense_list.html')

    def test_pagination(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)

    def test_lists_all_expenses(self):
        """
        Get second page and confirm it has remaining 3 items
        """
        response = self.client.get(reverse('expenses:expense-list')+'?page=2')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['expense_list']), 3)


class TestCategoryListView(TestCase):
    def set_up(self):
        self.client = Client()

    def test_url_exist(self):
        response = self.client.get('/expenses/category/list/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('expenses:category-list'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get('/expenses/category/list/')
        self.assertTemplateUsed(response, 'expenses/category_list.html')
