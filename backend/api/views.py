from .models import Post,Comment,PostImage,UserProfile
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer,PostSerializer,CommentSerializer,UserProfileSerializer
from rest_framework import status,generics,viewsets
from rest_framework.generics import CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from .serializers import ProfileSerializer,PostSerializer,PostViewSerializer,PostUpdateSerializer,PostImageSerializer,PostCreateSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return user_profile
    def perform_update(self, serializer):
        serializer.save()


class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return user



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return PostUpdateSerializer
        return PostSerializer
    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You can only update your own posts.")
        serializer.save()
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You can only delete your own posts.")
        instance.delete()




class AddCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        parent_id = self.request.data.get('parent')
        post = get_object_or_404(Post, id=post_id)
        parent_comment = None
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)
        serializer.save(post=post, author=self.request.user, parent=parent_comment)


class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            message = "You unliked this post."
        else:
            post.likes.add(user)
            message = "You liked this post."
        post.save()
        return Response(
            {
                "message": message,
                "like_count": post.likes.count(),
                "liked_by": [user.username for user in post.likes.all()]
            },
            status=status.HTTP_200_OK
        )


class ReplyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, comment_id):
        parent_comment = get_object_or_404(Comment, id=comment_id)
        reply_text = request.data.get('text')
        reply = Comment.objects.create(
            post=parent_comment.post,
            author=request.user,
            text=reply_text,
            parent=parent_comment
        )
        return Response(
            CommentSerializer(reply).data,
            status=status.HTTP_201_CREATED
        )


class ToggleLikeCommentView(APIView):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        user = request.user
        if user in comment.liked_comments.all():
            comment.liked_comments.remove(user)
            return Response({"message": "You unliked this comment.", "like_count": comment.like_count()}, status=status.HTTP_200_OK)
        else:
            comment.liked_comments.add(user)
            return Response({"message": "You liked this comment.", "like_count": comment.like_count()}, status=status.HTTP_200_OK)
