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


class TestExpenseCreateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Expense.objects.create(name='test expense1', amount=7.77)

    def set_up(self):
        self.client = Client()

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

    def set_up(self):
        self.client = Client()

    def test_delete_object(self):
        response = self.client.delete(reverse('expenses:expense-delete', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Expense.objects.all().count(), 0)


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
