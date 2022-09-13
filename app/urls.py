from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from app.api.viewsets import (AuthorViewSet, BookViewSet, CategoryViewSet,
                              PublishingCompanyViewSet)

app_name = 'app'

router = SimpleRouter()
router.register(
    'authors', AuthorViewSet, basename='author'
)
router.register(
    'categories', CategoryViewSet, basename='category'
)
router.register(
    'publishingcompanies', PublishingCompanyViewSet,
    basename='publishingcompany'
)
router.register(
    'books', BookViewSet, basename='book'
)

urlpatterns = [
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'
    ),
    path('', include(router.urls)),
]
