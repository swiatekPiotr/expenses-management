from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ..models import Category, Expense

import json


class TestExpenseListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for expense_id in range(8):
            Expense.objects.create(name='test {expense_id}', amount=8.88)
        return super().setUpTestData()

    def setUp(self):
        self.client = Client()
        return super().setUp()

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


class TestExpenseCreateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Expense.objects.create(name='test expense1', amount=7.77)
        return super().setUpTestData()

    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_post_new_object(self):
        """
        comparing the title of an existing object, with the one created using the post method
        """
        response = self.client.post(reverse('expenses:expense-create'), {
            'name': 'test expense2',
            'amount': 8.88
        })
        self.assertEquals(response.status_code, 200)
        test_expense1 = Expense.objects.get(id=1)
        self.assertNotEqual(test_expense1.name, 'test expense2')


class TestExpenseDeleteView(TestCase):
    @classmethod
    def setUpTestData(cls):
        category_1 = Category.objects.create(name='test category')
        Expense.objects.create(category=category_1, name='test expense', amount=6.69)
        return super().setUpTestData()

    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_delete_object(self):
        response = self.client.delete(reverse('expenses:expense-delete', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Expense.objects.all().count(), 0)


class TestCategoryListView(TestCase):
    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_url_exist(self):
        response = self.client.get('/expenses/category/list/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('expenses:category-list'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get('/expenses/category/list/')
        self.assertTemplateUsed(response, 'expenses/category_list.html')


class TestExpensesApi(APITestCase):
    def setUp(self):
        self.endpoint = '/expenses/api/'
        self.client = APIClient()

        category_1 = Category.objects.create(name='test category')
        self.expense_data = {
            'category': f'{category_1}',
            'name': 'test expense',
            'amount': 6.69
        }
        Expense.objects.create(
            category=category_1,
            name='test expense',
            amount=6.69
        )
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_method(self):
        response = self.client.get(path=self.endpoint)
        self.assertEquals(response.status_code, 200)
        print(json.loads(response.content))
        self.assertEquals(len(json.loads(response.content)), 1)
        self.assertEquals(response.json()[0]['amount'], '6.69')

    def test_post_method(self):
        response = self.client.post(path=self.endpoint, data=self.expense_data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Expense.objects.count(), 2)

    def test_retrieve_expense(self):
        response = self.client.get(path=self.endpoint+'1/')
        self.assertEquals(response.json()['amount'], '6.69')

    def test_destroy_expense(self):
        response = self.client.delete(path=self.endpoint + '1/')
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Expense.objects.count(), 0)
