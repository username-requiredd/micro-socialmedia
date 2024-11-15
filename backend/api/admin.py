from django.contrib import admin
from .models import Post,Comment,PostImage
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostImage)
