import React, { useState } from "react";
import { Heart, MessageCircle, Share2, MoreHorizontal, Send } from "lucide-react";
import Header from "../components/header";

const MicroSocialFeed = () => {
  const [posts, setPosts] = useState([
    {
      id: 1,
      author: "Sarah Chen",
      timestamp: "2m ago",
      content: "Just launched my new project! 🚀 Really excited to share it with everyone.",
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
    <>
    <Header/>
        <div className="max-w-xl mx-auto space-y-4 p-4">
      {/* New Post Input */}
      <div className="bg-white p-4 rounded-lg shadow">
        <div className="flex gap-4">
          <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center">
            <span className="text-sm font-medium text-white">You</span>
          </div>
          <input
            placeholder="What's on your mind?"
            className="flex-1 px-4 py-2 border rounded-lg text-sm"
          />
          <button className="px-4 py-2 bg-blue-500 text-white rounded-lg text-sm">
            Post
          </button>
        </div>
      </div>

      {/* Posts Feed */}
      {posts.map((post) => (
        <div key={post.id} className="bg-white p-4 rounded-lg shadow space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center">
                <span className="text-sm font-medium text-white">
                  {post.author
                    .split(" ")
                    .map((n) => n[0])
                    .join("")}
                </span>
              </div>
              <div>
                <p className="text-sm font-medium">{post.author}</p>
                <p className="text-xs text-gray-500">{post.timestamp}</p>
              </div>
            </div>
            <button className="p-2 text-gray-500">
              <MoreHorizontal className="h-4 w-4" />
            </button>
          </div>

          <p className="text-sm">{post.content}</p>

          <div className="flex items-center justify-between">
            <div className="flex space-x-4">
              <button
                className={`flex items-center text-sm ${post.isLiked ? "text-red-500" : "text-gray-500"}`}
                onClick={() => handleLike(post.id)}
              >
                <Heart className="h-4 w-4 mr-1" />
                {post.likes}
              </button>
              <button className="flex items-center text-sm text-gray-500">
                <MessageCircle className="h-4 w-4 mr-1" />
                {post.comments.length}
              </button>
              <button className="flex items-center text-sm text-gray-500">
                <Share2 className="h-4 w-4 mr-1" />
                Share
              </button>
            </div>
          </div>

          {/* Comments Section */}
          <div className="space-y-2">
            {post.comments.map((comment) => (
              <div key={comment.id} className="flex items-start space-x-2">
                <div className="w-6 h-6 rounded-full bg-gray-500 flex items-center justify-center">
                  <span className="text-xs text-white">
                    {comment.author
                      .split(" ")
                      .map((n) => n[0])
                      .join("")}
                  </span>
                </div>
                <div className="flex-1 bg-gray-100 rounded-lg p-2">
                  <p className="text-xs font-medium">{comment.author}</p>
                  <p className="text-sm">{comment.content}</p>
                </div>
              </div>
            ))}

            <div className="flex items-center space-x-2">
              <input
                placeholder="Write a comment..."
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
                className="flex-1 px-4 py-2 border rounded-lg text-sm"
              />
              <button onClick={() => handleComment(post.id)} className="p-2 bg-blue-500 rounded-full text-white">
                <Send className="h-4 w-4" />
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>

    </>
  );
};

export default MicroSocialFeed;
