from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .serializers import ReceiptSerializer, ItemSerializer
from .models import Receipt

from .utils import sum_points


class ReceiptProcess(APIView):
    """
    Creates a new Receipt and associated Items.
    Returns newly created Receipt's pk.
    """
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            items = request.data.pop('items')
            serializer = ReceiptSerializer(data=request.data)
            if serializer.is_valid():
                new_receipt = serializer.save()
                for item in items:
                    item['receipt'] = new_receipt.pk
                item_serializer = ItemSerializer(data=items, many=True)
                if item_serializer.is_valid():
                    item_serializer.save()
                    return Response({"id": new_receipt.pk}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

class ReceiptPoints(APIView):
    """
    Calculates and returns the number of points awarded from a
    specified Receipt.
    """
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Receipt.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"message": "Receipt does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            receipt = self.get_object(pk)
            points = sum_points(receipt, receipt.item_set.all())
            return Response({"points": points}, status=status.HTTP_200_OK)
        except receipt.DoesNotExist:
            return Response({"message": "Receipt does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"message": "Something went wrong.  Please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
