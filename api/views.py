from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status

from .models import Listing, Category
from .serializers import ListingSerializer, CategorySerializer
# Create your views here.

class Apis(APIView):
    # http_method_names = ['put', 'delete']
	
    def get(self, request):
        print(request)
        return Response({"message": "Hello, World!"})

    def post(self, request):
        print(request.data)
        return Response({"message": "Hello, World!"})
    
class BookView(viewsets.ViewSet):
	
	def tout(self, request):
		return Response({"message":"All books"}, status.HTTP_200_OK)
	def create(self, request):
		return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
	def update(self, request, pk=None):
		return Response({"message":"Updating a book"}, status.HTTP_200_OK)
	def retrieve(self, request, pk=None):
		return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
	def partial_update(self, request, pk=None):
		return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
	def destroy(self, request, pk=None):
		return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
	
class ListingView(viewsets.ModelViewSet):

    queryset = Listing.objects.select_related().all()
    serializer_class = ListingSerializer
	
class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer