from rest_framework import serializers
from .models import Post
from api.comments.models import Comment
from api.comments.serializers import CommentsSerializer
from django.contrib.auth import get_user_model
    
class PostSerializer(serializers.ModelSerializer):
    comments  = CommentsSerializer(read_only=True, many=True)
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at','comments')
        model = Post

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
      model = get_user_model()
      fields = ('id', 'username',)