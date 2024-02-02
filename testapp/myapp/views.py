from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def test(request):
    return HttpResponse('<h1>Test</h1>')


class ItemView(APIView):

    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pass

    def delete(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
