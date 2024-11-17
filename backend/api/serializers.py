from rest_framework import serializers
from .models import Post,Comment,PostImage,ChatRoom,Message
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import get_object_or_404


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp']
        read_only_fields = ['sender', 'room']

    def create(self, validated_data):
        room_id = self.context['view'].kwargs['room_id']
        room = get_object_or_404(ChatRoom, id=room_id)
        validated_data['sender'] = self.context['request'].user
        validated_data['room'] = room
        return super().create(validated_data)

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'participants', 'created_at']

    def validate_participants(self, value):
        if len(value) != 2:
            raise serializers.ValidationError("Direct messaging requires exactly two participants.")
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'gender', 'studied_at','city','birth_date','relationship_status',]

class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'posts']

    def get_profile_picture(self, user):
        user_profile = user.userprofile
        return user_profile.profile_picture.url if user_profile.profile_picture else None

    def get_posts(self, user):
        user_posts = Post.objects.filter(author=user)
        return PostSerializer(user_posts, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'created_at','replies', 'like_count']
        read_only_fields = ['post', 'author', 'created_at', 'like_count', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
    def get_like_count(self, obj):
        return obj.liked_comments.count()

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author','images', 'comments', 'like_count']
    def get_like_count(self, obj):
        return obj.likes.count()


class PostCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'images']
    def create(self, validated_data):
        images = validated_data.pop('images', [])
        post = Post.objects.create(author=self.context['request'].user, **validated_data)
        for image in images:
            PostImage.objects.create(post=post, image=image)
        return post
class PostViewSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    class Meta:
        model = Post
        fields = ['title', 'body', 'author', 'images']
        read_only_fields = ['author']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        UserProfile.objects.create(user=user)
        return user

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author']
        read_only_fields = ['author']


