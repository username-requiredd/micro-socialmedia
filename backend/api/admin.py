from django.contrib import admin
from .models import Post,Comment,PostImage,ChatRoom,Message
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostImage)
admin.site.register(ChatRoom)
admin.site.register(Message)