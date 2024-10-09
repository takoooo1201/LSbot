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
    <p>this is a website designed to deal with the information about land subsidence on internet</p>
    <!-- Check MongoDB Connection Button -->
    <div class="buttons-column">
      <button @click="checkConnection" class="textured-button" :disabled="isLoading">
        <span v-if="isLoading" class="loader"></span>
        <span v-else>Check MongoDB Connection</span>
      </button>
      <p>//check if the database is connected successfully</p>

      <!-- Ping Responsebot Button -->
      <button @click="pingResponsebot" class="textured-button" :disabled="isPinging">
        <span v-if="isPinging" class="loader"></span>
        <span v-else>Ping Responsebot</span>
      </button>
      <span v-if="pingSuccess" class="check-mark">✅</span>
      <p>//ping reponsebot </p>


      <!-- Ping Backend Button -->
      <button @click="pingBackend" class="textured-button" :disabled="isPingingBackend">
        <span v-if="isPingingBackend" class="loader"></span>
        <span v-else>Ping Backend</span>
      </button>
      <p>//ping the backend to check if it is activated</p>

      <!-- Navigation Buttons -->
      <button @click="redirectToDaily" class="textured-button">Daily</button>
      <p>//show all the posts which are crawled down fron Dcard that day</p>
      <button @click="redirectToTodoList" class="textured-button">To Do List</button>
      <p>//only the posts which are related to land subsidence will be shown with AI explanation and sentiment analysis( filterd by the relation model GPT)</p>
      <button @click="redirectToResponseGPT" class="textured-button">ResponseGPT</button>
      <p>//A GPT which can generate official reponses according to the land subsidence posts</p>

    </div>
    <!-- Check MongoDB Connection Button
    <button @click="checkConnection" class="textured-button" :disabled="isLoading">
      <span v-if="isLoading" class="loader"></span>
      <span v-else>Check MongoDB Connection</span>
    </button> -->

    <!-- Ping Responsebot Button -->
    <!-- <div class="ping-responsebot-container">
      <button @click="pingResponsebot" class="textured-button" :disabled="isPinging">
        <span v-if="isPinging" class="loader"></span>
        <span v-else>Ping Responsebot</span>
      </button>
      <span v-if="pingSuccess" class="check-mark">✅</span>
    </div> -->

    <!-- Navigation Buttons -->
    <!-- <div class="navigation-buttons">
      <div>
      <button @click="redirectToDaily" class="textured-button">Daily</button>
      </div>
      
      <div>
      <button @click="redirectToTodoList" class="textured-button">To Do List</button>
      </div>
      <div>
      <button @click="redirectToResponseGPT" target="_blank" class="textured-button">ResponseGPT</button>
      </div>
    </div> -->

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
        const response = await axios.get('https://lsbotbackend.onrender.com/check-connection');
        if (response.status === 200) {
          alert('connect success');
        }
      } catch (error) {
        alert(`Error: ${error.response?.data?.error || 'Connection failed'}`);
      } finally {
        this.isLoading = false;
      }
    },
    // async pingResponsebot() {
    //   this.isPinging = true;
    //   this.pingSuccess = false; // Reset success indicator before making the request
    //   try {
    //     // Perform a ping by making a GET request, without caring about the response
    //     await axios.get('https://landsubsidencegpt.onrender.com', { timeout: 100 });
    //     this.pingSuccess = true; // Indicate ping success
    //   } catch {
    //     // Optionally handle error (e.g., silently fail or provide minimal feedback)
    //     this.pingSuccess = true; // Ensure no success mark if it failed
    //   } finally {
    //     this.isPinging = false; // Stop the loading state
    //   }
    // },
    async pingBackend() {
      this.isPingingBackend = true;
      try {
        const response = await axios.get('https://lsbotbackend.onrender.com/ping');
        if (response.status === 200) {
          alert('backend activated');
        }
      } catch (error) {
        alert(`Error: ${error.response?.data?.error || 'Ping failed'}`);
      } finally {
        this.isPingingBackend = false;
      }
    },



    // direct function
    redirectToDaily() {
      this.$router.push('/daily');
    },
    redirectToTodoList() {
      this.$router.push('/todo');
    },
    redirectToResponseGPT() {
      window.location.href = 'https://landsubsidencegpt.onrender.com';
    },
  },
};
</script>

<style scoped>

.buttons-column {
  display: flex;
  flex-direction: column; /* Align buttons in a column */
  gap: 15px; /* Space between buttons */
  margin-top: 20px;
}
.textured-button {
  background: #47974a;
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

.navigation-buttons {
  margin-top: 20px;
  display: flex;
  gap: 10px; /* Space between buttons */
  flex-wrap: wrap; /* Wrap buttons if the screen is small */
}
</style>
