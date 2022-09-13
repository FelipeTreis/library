from app.models import Book, Category, PublishingCompany
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class PublishingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingCompany
        fields = (
            'id',
            'name',
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'state',
            'category',
            'publishing_company',
        )
