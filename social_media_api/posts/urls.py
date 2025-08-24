from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, FeedView

# DRF routers for Post and Comment viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# Add feed route
urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
]
