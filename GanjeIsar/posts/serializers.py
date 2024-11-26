from rest_framework import serializers

from .models import Post ,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text','created_time','post']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','title','text','avatar','created_time']