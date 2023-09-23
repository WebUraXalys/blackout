from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CardsSerializer
from .models import Cards



class ChangeCardApiView(RetrieveUpdateDestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['id'])
        return obj


class CreateCardsApiView(ListCreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cards.objects.filter(Owner=self.request.user)


    def list(self, request):
        queryset = self.get_queryset()
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)
