from rest_framework.views import APIView
from .models import Post
from .serializers import *
from rest_framework.response import Response
import requests

class PostView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        #return Response([self.format(p) for p in posts])
        return Response(serializer.data)
    
    def format(self, post):
        comments = requests.get('http://localhost:8001/api/posts/%d/comments' % post.id).json()
        return{
            'id':post.id,
            'title':post.title,
            'description':post.description,
            'comments': comments
        }
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)