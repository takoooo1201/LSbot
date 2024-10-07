import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/LoginPage.vue';
import Home from '../views/HomePage.vue';
import Daily from '../views/DailyPage.vue';
import Todo from '../views/TodoPage.vue';

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/home', name: 'Home', component: Home },
  { path: '/daily', name: 'Daily', component: Daily },
  { path: '/todo', name: 'Todo', component: Todo },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
