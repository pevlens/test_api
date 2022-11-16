
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, TransactionsUser


class CategorySerializer(ModelSerializer):

    user = serializers.CharField(source = 'user.username')
    class Meta:
        model = Category
        fields = ('__all__')

    def create(self, validated_data):
        request = self.context.get("request")
        cr = Category.objects.create(user=request.user, name=validated_data['name'])
        return cr


class TransactionSerealazer(ModelSerializer):

    person = serializers.CharField(source = 'person.username', read_only=True)
#    cat = serializers.CharField(source = 'cat.name')

    class Meta:
        model = TransactionsUser
        fields = ("__all__")
#       depth = 1
    
    def create(self, validated_data):
        request = self.context.get("request")
        cr = TransactionsUser.objects.create(person=request.user, summ=validated_data['summ'], cat=validated_data['cat'], about=validated_data['about'], organisations=validated_data['organisations'])
        return cr
