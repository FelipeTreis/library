from django.contrib import admin

from app.models import Book, Category, PublishingCompany


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )


@admin.register(PublishingCompany)
class PublishingCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('is_available', 'name', 'state', 'added_at', )
    list_display_links = ('name', )
    list_filter = ('name', 'state', 'category', 'publishing_company', )
    list_editable = ('is_available', )
    list_per_page = 10
    search_fields = ('name', 'state', 'category', 'publishing_company', )
    autocomplete_fields = ('category', 'publishing_company', )
