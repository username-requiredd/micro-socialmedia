from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import PostViewSet,register_user,AddCommentView,ToggleLikeView
from .views import ReplyView,ToggleLikeCommentView, ProfileView,UserProfileUpdateView,ChatRoomListCreateView,MessageListCreateView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user, name='register_user'),
    path('posts/<int:post_id>/comments/', AddCommentView.as_view(), name='add_comment'),
    path('posts/<int:post_id>/like/', ToggleLikeView.as_view(), name='toggle-like'),
    path('comments/<int:comment_id>/reply/', ReplyView.as_view(), name='add-reply'),
    path('comments/<int:comment_id>/like/', ToggleLikeCommentView.as_view(), name='toggle-like-comment'),
    path('profile/<str:username>/', ProfileView.as_view(), name='user-profile'),
    path('chat/rooms/', ChatRoomListCreateView.as_view(), name='chat_room_list_create'),
    path('chat/rooms/<int:room_id>/messages/', MessageListCreateView.as_view(), name='message_list_create'),
    path('', include(router.urls)),
]


