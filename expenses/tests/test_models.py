from django.test import TestCase
from ..models import Category, Expense


class TestExpenseModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        category_1 = Category.objects.create(name='test category')
        Expense.objects.create(category=category_1, name='test', amount=8.88)

    def test_name_label(self):
        expense = Expense.objects.get(id=1)
        field_label = expense._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        expense = Expense.objects.get(id=1)
        max_length = expense._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_date_not_none(self):
        expense = Expense.objects.get(id=1)
        self.assertNotEqual(expense.date, None)

    def test_object_str_method(self):
        expense = Expense.objects.get(id=1)
        expected_obj_name = f"{expense.date} {expense.name} {expense.amount}"
        self.assertEqual(str(expense), expected_obj_name)


class TestCategoryModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='test category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_object_str_method(self):
        category = Category.objects.get(id=1)
        expected_obj_name = f"{category.name}"
        self.assertEqual(str(category), expected_obj_name)
