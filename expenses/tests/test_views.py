from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Expense


class TestExpenseListView(TestCase):
    def set_up(self):
        self.client = Client()

    def test_url_exist(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('expense-list'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertTemplateUsed(response, 'expenses/expense_list.html')

    def test_pagination(self):
        response = self.client.get('/expenses/expense/list/')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
