from app.api.serializers import (BookSerializer, CategorySerializer,
                                 PublishingCompanySerializer)
from app.models import Book, Category, PublishingCompany
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = Pagination


class PublishingCompanyViewSet(viewsets.ModelViewSet):
    queryset = PublishingCompany.objects.all()
    serializer_class = PublishingCompanySerializer
    pagination_class = Pagination


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    pagination_class = Pagination
