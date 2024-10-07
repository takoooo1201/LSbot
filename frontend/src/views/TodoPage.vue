<template>
    <div class="forum-container">
      <h1>Content related to land subsidence</h1>

      <!-- Loading Spinner -->
      <div v-if="isLoading" class="loading-spinner"></div>
      
      <div v-for="(post, index) in dailyContent" :key="index" class="post-card">
        <div class="post-header">
          <h3 class="post-title">{{ post.title }}</h3>
          <p class="post-meta">
            <span class="author">By: {{ post.author }}</span> | 
            <span class="date">{{ post.date }}</span>
          </p>
        </div>
        <div class="post-content">
          <p>{{ post.content }}</p>
        </div>
        <div class="post-tags">
          <span class="tag">{{ post.tag }}</span>
        </div>
        <div class="post-footer">
          <span class="emoji">❤️Emoji: {{ post.emojiNum === "愛心" ? 0 : post.emojiNum }}</span>
          <span class="collect">🔖Collection: {{ post.collectNum === "收藏" ? 0 : post.collectNum }}</span>
          <span class="comments">💬Comments: ({{ post.comments.length }})</span>
        </div>
        <!-- Explanation Section -->
        <div class="explanation-section" v-if="post.explanation">
          <h4>AI Explanation:</h4>
          <p>{{ post.explanation }}</p>
        </div>
        <div class="explanation-section" v-if="post.negRatio">
          <h4>comments sentiment analysis:</h4>
          <p>Negative Ratio: {{ post.negRatio }}</p>
        </div>
        <!-- Comments Section -->
        <div class="comments-section" v-if="post.comments.length > 0">
          <h4>Comments</h4>
          <ul>
            <li v-for="(comment, cIndex) in post.comments" :key="cIndex" class="comment">
              {{post.comments_sentiment[cIndex]}}||:{{ comment }}
            </li>
          </ul>
        </div>
        <a :href="post.href" target="_blank" class="read-more">Read More</a>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dailyContent: [],
        isLoading: true,  // Loading state
      };
    },
    async created() {
      try {
        const response = await axios.get('https://lsbotbackend.onrender.com/todo');
        const { data, explain } = response.data;
  
        this.dailyContent = data.map((post, index) => ({
          ...post,
          explanation: explain[index] || "No explanation available",
        }));
      } catch (error) {
        console.error('Error fetching daily content:', error);
      } finally {
        this.isLoading = false;  // Hide loading spinner when done
      }
    },
  };
  </script>
  
  <style scoped>
  .forum-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .post-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .post-header {
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 10px;
    margin-bottom: 15px;
  }
  
  .post-title {
    margin: 0;
    font-size: 1.5em;
    color: #333;
  }
  
  .post-meta {
    font-size: 0.9em;
    color: #777;
  }
  
  .post-content {
    margin-bottom: 15px;
    font-size: 1em;
    color: #444;
    line-height: 1.6;
  }
  
  .post-tags {
    margin-bottom: 15px;
  }
  
  .tag {
    display: inline-block;
    background-color: #e0e0e0;
    color: #555;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 0.9em;
  }
  
  .post-footer {
    display: flex;
    justify-content: space-between;
    font-size: 0.9em;
    color: #555;
  }
  
  .emoji, .collect, .comments {
    margin-right: 10px;
  }
  
  .comments-section {
    margin-top: 15px;
    border-top: 1px solid #f0f0f0;
    padding-top: 15px;
  }
  
  .comments-section h4 {
    margin: 0;
    font-size: 1.2em;
    color: #333;
  }
  
  /* .comment {
    list-style: none;
    padding: 10px 0;
    border-bottom: 1px solid #f0f0f0;
    color: #444;
  } */
  .comment {
    list-style: none;
    padding: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    margin-bottom: 10px;
    background-color: #f9f9f9;
  } 
  /* .comment {
    list-style: none;
    padding: 10px;
  } */
  
  .comment-separator {
    border-bottom: 1px solid #e0e0e0;
    margin: 10px 0;
  }
  
  .comment:last-child {
    border-bottom: none;
  }
  
  .read-more {
    display: inline-block;
    margin-top: 15px;
    padding: 10px 15px;
    background-color: #3498db;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s;
  }
  
  .read-more:hover {
    background-color: #2980b9;
  }
  .explanation-section {
  margin-top: 10px;
  padding: 10px;
  background-color: #f8f8f8;
  border-left: 3px solid #3498db;
  font-style: italic;
}

/* Loading Spinner */
.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 50px auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

  </style>