from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().prefetch_related('comment_set')
    serializer_class = PostSerializer

    filterset_fields = ['title', 'created_at']
    search_fields = ['title', 'content']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
