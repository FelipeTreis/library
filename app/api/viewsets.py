from app.api.serializers import BookSerializer
from app.models import Book
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book
    serializer_class = BookSerializer
    pagination_class = Pagination
