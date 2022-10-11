import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Registration from "../views/Registration";
import Auth from "../views/Auth";
import Feed from "../views/Feed";
import Notification from "../views/Notification";
import Profile from "../views/Profile";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed
  },
  {
    path: '/notification',
    name: 'Notification',
    component: Notification
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
