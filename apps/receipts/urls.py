from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.receipts import views

urlpatterns = [
    path('receipts/<int:pk>/points', views.ReceiptPoints.as_view()),
    path('receipts/process', views.ReceiptProcess.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)