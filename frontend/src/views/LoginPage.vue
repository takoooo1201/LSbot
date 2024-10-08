<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" type="text" placeholder="Username" />
        <br>
        <input v-model="password" type="password" placeholder="Password" />
        <br>
        <button type="submit">Login</button>
      </form>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        message: '',
      };
    },
    methods: {
      async handleLogin() {
        try {
          const response = await axios.post('https://lsbotbackend.onrender.com/login', {
            username: this.username,
            password: this.password,
          });
          this.message = response.data.message;
          this.$router.push('/home');
        } catch (error) {
          this.message = error.response.data.message;
        }
      },
    },
  };
  </script>
  