import React, { useState } from "react";
import {
  Heart,
  MessageCircle,
  Share2,
  MoreHorizontal,
  Send,
} from "lucide-react";
import {
  Card,
  CardHeader,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Avatar } from "@/components/ui/avatar";
import { Input } from "@/components/ui/input";

const MicroSocialFeed = () => {
  const [posts, setPosts] = useState([
    {
      id: 1,
      author: "Sarah Chen",
      timestamp: "2m ago",
      content:
        "Just launched my new project! 🚀 Really excited to share it with everyone.",
      likes: 12,
      comments: [
        {
          id: 1,
          author: "Alex Kim",
          content: "Congratulations! Can't wait to see it!",
        },
      ],
      isLiked: false,
    },
    {
      id: 2,
      author: "Marcus Johnson",
      timestamp: "15m ago",
      content: "Beautiful sunset at the beach today 🌅",
      likes: 8,
      comments: [],
      isLiked: false,
    },
  ]);

  const [newComment, setNewComment] = useState("");

  const handleLike = (postId) => {
    setPosts(
      posts.map((post) => {
        if (post.id === postId) {
          return {
            ...post,
            likes: post.isLiked ? post.likes - 1 : post.likes + 1,
            isLiked: !post.isLiked,
          };
        }
        return post;
      })
    );
  };

  const handleComment = (postId) => {
    if (!newComment.trim()) return;

    setPosts(
      posts.map((post) => {
        if (post.id === postId) {
          return {
            ...post,
            comments: [
              ...post.comments,
              {
                id: post.comments.length + 1,
                author: "You",
                content: newComment,
              },
            ],
          };
        }
        return post;
      })
    );
    setNewComment("");
  };

  return (
    <div className="max-w-xl mx-auto space-y-4 p-4">
      {/* New Post Input */}
      <Card className="bg-white">
        <CardContent className="pt-4">
          <div className="flex gap-4">
            <Avatar className="w-10 h-10 bg-blue-500">
              <span className="text-sm font-medium">You</span>
            </Avatar>
            <div className="flex-1">
              <Input placeholder="What's on your mind?" className="w-full" />
            </div>
            <Button size="sm">Post</Button>
          </div>
        </CardContent>
      </Card>

      {/* Posts Feed */}
      {posts.map((post) => (
        <Card key={post.id} className="bg-white">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <div className="flex items-center space-x-4">
              <Avatar className="w-10 h-10 bg-blue-500">
                <span className="text-sm font-medium">
                  {post.author
                    .split(" ")
                    .map((n) => n[0])
                    .join("")}
                </span>
              </Avatar>
              <div>
                <p className="text-sm font-medium">{post.author}</p>
                <p className="text-xs text-gray-500">{post.timestamp}</p>
              </div>
            </div>
            <Button variant="ghost" size="icon">
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </CardHeader>

          <CardContent>
            <p className="text-sm">{post.content}</p>
          </CardContent>

          <CardFooter className="flex flex-col space-y-4">
            <div className="flex items-center justify-between w-full">
              <div className="flex space-x-4">
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => handleLike(post.id)}
                  className={post.isLiked ? "text-red-500" : ""}
                >
                  <Heart className="h-4 w-4 mr-2" />
                  {post.likes}
                </Button>
                <Button variant="ghost" size="sm">
                  <MessageCircle className="h-4 w-4 mr-2" />
                  {post.comments.length}
                </Button>
                <Button variant="ghost" size="sm">
                  <Share2 className="h-4 w-4 mr-2" />
                  Share
                </Button>
              </div>
            </div>

            {/* Comments Section */}
            <div className="w-full space-y-2">
              {post.comments.map((comment) => (
                <div key={comment.id} className="flex items-start space-x-2">
                  <Avatar className="w-6 h-6 bg-gray-500">
                    <span className="text-xs">
                      {comment.author
                        .split(" ")
                        .map((n) => n[0])
                        .join("")}
                    </span>
                  </Avatar>
                  <div className="flex-1 bg-gray-100 rounded-lg p-2">
                    <p className="text-xs font-medium">{comment.author}</p>
                    <p className="text-sm">{comment.content}</p>
                  </div>
                </div>
              ))}

              <div className="flex items-center space-x-2">
                <Input
                  placeholder="Write a comment..."
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                  className="flex-1 text-sm"
                />
                <Button size="icon" onClick={() => handleComment(post.id)}>
                  <Send className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
};

export default MicroSocialFeed;
