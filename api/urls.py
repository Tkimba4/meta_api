from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter(True)
router.register('books', views.BookView, basename='book')
router.register('livres', views.BookView, basename='livres')
router.register('listings', views.ListingView, basename='listing')
router.register('categories', views.CategoryView, basename='category')
urlpatterns = [
    path('book/', views.Listings.as_view()),
]

urlpatterns += router.urls
