from rest_framework import filters
from rest_framework import viewsets
from .models import Category, TransactionsUser
from .serializers import CategorySerializer, TransactionSerealazer
from rest_framework.views import APIView
from rest_framework.response import Response
from .filter import Filter
from django.contrib.auth.models import AnonymousUser






class CategoryViewSets(viewsets.ModelViewSet):
    serializer_class  = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)



class TransactionViewSets(viewsets.ModelViewSet):
    serializer_class = TransactionSerealazer
    filterset_class = Filter
    ordering_fields = ['summ', 'time', 'date']
    

    def get_queryset(self):
        return TransactionsUser.objects.filter(person = self.request.user)



class BalanseUser(APIView):

    def get(self, request, format = None):
        if request.user != AnonymousUser():
            summ  = sum([i.summ for i in TransactionsUser.objects.filter(person = request.user)])
            user = str(request.user)
            return Response({"balanse": summ, "user": user})
        else:
            return Response("not auth")
    
    