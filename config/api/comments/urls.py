
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import  CommentsViewSet

router = SimpleRouter()

router.register('', CommentsViewSet, basename='comment')

urlpatterns = router.urls