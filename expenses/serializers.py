from rest_framework import serializers


class ExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    name = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    date = serializers.DateField()
