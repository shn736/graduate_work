from django.urls import include, path
from rest_framework.routers import DefaultRouter

from library.apps import LibraryConfig
from library.views import (AuthorCreateApiView, AuthorDestroyApiView,
                           AuthorListApiView, AuthorRetrieveApiView,
                           AuthorUpdateApiView, BookLoanViewSet, BookViewSet)

app_name = LibraryConfig.name


router = DefaultRouter()
router.register(r"books", BookViewSet, "books")
router.register(r"loans", BookLoanViewSet, "loans")

urlpatterns = [
    path("api/", include(router.urls)),
    path("author/", AuthorListApiView.as_view(), name="author-list"),
    path("author/<int:pk>/", AuthorRetrieveApiView.as_view(), name="author-detail"),
    path("author/create/", AuthorCreateApiView.as_view(), name="author-create"),
    path(
        "author/<int:pk>/delete/", AuthorDestroyApiView.as_view(), name="author-delete"
    ),
    path(
        "author/<int:pk>/update/", AuthorUpdateApiView.as_view(), name="author-update"
    ),
]

urlpatterns += router.urls
