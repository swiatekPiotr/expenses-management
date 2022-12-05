from rest_framework import serializers
from .models import Expense, Category


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=False,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Expense
        fields = '__all__'
