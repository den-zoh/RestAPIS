from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_create_api_view
from news.api.views import ArticleDetailAPIView, ArticleListCreateView, JournalistListCreateAPIView

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list"),
    
]