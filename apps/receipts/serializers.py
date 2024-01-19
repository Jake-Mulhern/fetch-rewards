from rest_framework import serializers

from apps.receipts.models import Receipt, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'shortDescription', 'price', 'receipt']

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = ['id', 'retailer', 'purchaseDate', 'purchaseTime', 'total']
