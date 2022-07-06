from rest_framework import serializers
from .models import Comment

    
class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'post', 'name', 'email', 'body','created_on',)
        model = Comment

