from rest_framework.views import APIView
from .serializers import CommentSerializer
from rest_framework.response import Response
from .models import Comment

class CommentByPost(APIView):
    def get(self, _, pk=None):
        comments = Comment.objects.filter(postID=pk)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

class CommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

