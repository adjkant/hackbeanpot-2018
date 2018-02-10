// Basics
import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios';

// Pages
import Splash from '@/components/pages/Splash'
import About from '@/components/pages/About'
import Register from '@/components/pages/Register'
import Login from '@/components/pages/Login'
import Home from '@/components/pages/Home'
import Profile from '@/components/pages/Profile'
import ProfileEdit from '@/components/pages/ProfileEdit'
import Search from '@/components/pages/Search'
import Company from '@/components/pages/Company'
import Review from '@/components/pages/Review'
import Page404 from '@/components/pages/Page404'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component: Splash
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/home',
      component: Home,
      beforeEnter: requireAuth
    },
    {
      path: '/profile',
      component: Profile,
      beforeEnter: requireAuth
    },
    {
      path: '/profile/edit',
      component: ProfileEdit,
      beforeEnter: requireAuth
    },
    {
      path: '/search',
      component: Search,
      beforeEnter: requireAuth
    },
    {
      path: '/company/:id',
      component: Company,
      beforeEnter: requireAuth
    },
    {
      path: '/company/:id/:jobId',
      component: Company,
      beforeEnter: requireAuth
    },
    {
      path: '/review',
      component: Review,
      beforeEnter: requireAuth
    },
    {
      path: '*',
      component: Page404
    }
  ]
})

function requireAuth (to, from, next) {
  let instance = axios.create({
    baseURL: 'http://localhost:5000/api/'
  });

  let thing = {
    a: "a"
  };

  instance.post('/user/login/check', thing, {withCredentials: true})
    .then(response => {
      next();
    })
    .catch(error => {
      next({
        path: from.fullPath
      });
    });



}