from app.models import Author, Book, Category, PublishingCompany
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'full_name',
        )


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
            'language',
            'author',
            'publishing_company',
        )
