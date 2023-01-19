from django.urls import path
from .views import ItemListAPIView, ItemDetailAPIView, CommentAPIView, FavoriteAPIView, FillAPIView

urlpatterns = [
        path('', ItemListAPIView.as_view()),
        path('<int:pk>/', ItemDetailAPIView.as_view()),
        path('<int:pk>/favorite/', FavoriteAPIView.as_view()),
        path('<int:pk>/comment/', CommentAPIView.as_view()),
        path('favorite/', FavoriteAPIView.as_view()),
        path('fill/', FillAPIView.as_view())
]
