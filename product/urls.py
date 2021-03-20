from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view()),
    path("create/", ProductCreateView.as_view()),
    path("detail/<int:pk>/", ProductDetailView.as_view()),
]
