from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    bio = models.TextField(
        verbose_name="Biography",
        max_length=500,
        blank=True,
        null=True,
        help_text="A short description about yourself (up to 500 characters)."
    )


    studied_at = models.CharField(
        verbose_name="Education",
        max_length=100,
        blank=True,
        null=True,
        help_text="Where did you study?"
    )


    city = models.CharField(
        verbose_name="City of Residence",
        max_length=100,
        blank=True,
        null=True,
        help_text="City where you currently reside."
    )

    # Gender choices with select options
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        help_text="Select your gender."
    )

    # Birthdate with validation
    birth_date = models.DateField(
        verbose_name="Date of Birth",
        blank=True,
        null=True,
        help_text="Please use the following format: YYYY-MM-DD."
    )

    # Relationship status choices
    RELATIONSHIP_STATUS_CHOICES = [
        ('single', 'Single'),
        ('in_a_relationship', 'In a Relationship'),
        ('married', 'Married'),
        ('complicated', 'It’s Complicated'),
    ]
    relationship_status = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_STATUS_CHOICES,
        blank=True,
        null=True,
        help_text="Select your current relationship status."
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)


    def __str__(self):
        return f"{self.title} - Likes: {self.likes.count()}"

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/kojo_pic/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    liked_comments = models.ManyToManyField(User, related_name='like_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Comment by {self.author} on {self.post} - Likes: {self.liked_comments.count()}"

    @property
    def is_reply(self):
        return f"Comment by {self.author} on {self.post} - {'Reply' if self.parent else 'Parent'}"

    def like_count(self):
        return self.liked_comments.count()


class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.id} - Participants: {', '.join([user.username for user in self.participants.all()])}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Message by {self.sender.username} in Room {self.room.id} at {self.timestamp}"