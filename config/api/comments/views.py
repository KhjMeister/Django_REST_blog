from rest_framework.permissions import AllowAny
from rest_framework import viewsets 
from .models import Comment
from .serializers import CommentsSerializer
from .permissions import IsAuthorOrReadOnly

class CommentsViewSet(viewsets.ModelViewSet): 
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Comment.objects.all()
	serializer_class = CommentsSerializer

