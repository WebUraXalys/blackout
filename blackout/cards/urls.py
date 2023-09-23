from django.urls import path
from .views import CreateCardsApiView, ChangeCardApiView

urlpatterns = [
    path('cards/<int:id>/', ChangeCardApiView.as_view(), name='Cards_detail'),
    path('cards/', CreateCardsApiView.as_view(), name='Cards'),
]
