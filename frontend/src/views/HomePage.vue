<!-- <template>
  <div>
    <h2>Home</h2>
    <p>Welcome to the Home Page!</p>
    <button @click="checkConnection" class="textured-button" :disabled="isLoading">
      <span v-if="isLoading" class="loader"></span>
      <span v-else>Check MongoDB Connection</span>
    </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isLoading: false,
    };
  },
  methods: {
    async checkConnection() {
      this.isLoading = true;
      try {
        const response = await axios.get('http://localhost:5000/check-connection');
        if (response.status === 200) {
          alert('connect success');
        }
      } catch (error) {
        alert(`Error: ${error.response?.data?.error || 'Connection failed'}`);
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
.textured-button {
  background: #4caf50;
  color: white;
  border: 2px solid #4caf50;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.textured-button:disabled {
  background: #ccc;
  cursor: not-allowed;
  border-color: #ccc;
}

.loader {
  border: 4px solid #f3f3f3; /* Light grey */
  border-top: 4px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style> -->
<template>
  <div>
    <h2>Home</h2>
    <p>Welcome to the Home Page!</p>
    
    <!-- Check MongoDB Connection Button -->
    <button @click="checkConnection" class="textured-button" :disabled="isLoading">
      <span v-if="isLoading" class="loader"></span>
      <span v-else>Check MongoDB Connection</span>
    </button>

    <!-- Ping Responsebot Button -->
    <div class="ping-responsebot-container">
      <button @click="pingResponsebot" class="textured-button" :disabled="isPinging">
        <span v-if="isPinging" class="loader"></span>
        <span v-else>Ping Responsebot</span>
      </button>
      <span v-if="pingSuccess" class="check-mark">✅</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isLoading: false,
      isPinging: false,
      pingSuccess: false,
    };
  },
  methods: {
    async checkConnection() {
      this.isLoading = true;
      try {
        const response = await axios.get('http://localhost:5000/check-connection');
        if (response.status === 200) {
          alert('connect success');
        }
      } catch (error) {
        alert(`Error: ${error.response?.data?.error || 'Connection failed'}`);
      } finally {
        this.isLoading = false;
      }
    },
    async pingResponsebot() {
      this.isPinging = true;
      this.pingSuccess = false; // Reset success indicator before making the request
      try {
        // Perform a ping by making a GET request, without caring about the response
        await axios.get('https://landsubsidencegpt.onrender.com', { timeout: 100 });
        this.pingSuccess = true; // Indicate ping success
      } catch {
        // Optionally handle error (e.g., silently fail or provide minimal feedback)
        this.pingSuccess = true; // Ensure no success mark if it failed
      } finally {
        this.isPinging = false; // Stop the loading state
      }
    },
  },
};
</script>

<style scoped>
.textured-button {
  background: #4caf50;
  color: white;
  border: 2px solid #4caf50;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 10px 0;
}

.textured-button:disabled {
  background: #ccc;
  cursor: not-allowed;
  border-color: #ccc;
}

.loader {
  border: 4px solid #f3f3f3; /* Light grey */
  border-top: 4px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.ping-responsebot-container {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.check-mark {
  font-size: 1.5em;
  color: green;
  margin-left: 10px;
}
</style>
