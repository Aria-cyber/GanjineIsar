

from django.http import Http404

from rest_framework.views import APIView
from  rest_framework import status
from  rest_framework.response import Response

from .models import Post , Comment
from .serializers import PostSerializer , CommentSerializer


# def get(self,request , pk):
#     post = self.get_post(pk)
#
#     serializer = PostSerializer(post).data
#     return Response(serializer)

class PostDetailView(APIView):


    def get(self,request , pk):

         postcomment = Comment.objects.filter(post=pk)
         serializer = CommentSerializer(postcomment , many=True)
         return Response(serializer.data)


    def post(self ,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self,request , pk):
        post = self.get_post(pk)

        serializer = PostSerializer(post , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,pk):
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def get_post(self,pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        return post


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
