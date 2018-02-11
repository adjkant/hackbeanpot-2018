// Basics
import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios';

Vue.use(require('vue-cookies'));
import VueCookies from 'vue-cookies';

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
import ReviewInfo from '@/components/pages/ReviewInfo'
import Page404 from '@/components/pages/Page404'

Vue.use(Router);
Vue.use(VueCookies);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'splash',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      beforeEnter: requireAuth
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
      beforeEnter: requireAuth
    },
    {
      path: '/profile/edit',
      name: 'profile-edit',
      component: ProfileEdit,
      beforeEnter: requireAuth
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      beforeEnter: requireAuth
    },
    {
      path: '/company/:id',
      name: 'company',
      component: Company,
      beforeEnter: requireAuth
    },
    {
      path: '/company/:id/:jobId',
      name: 'company-job',
      component: Company,
      beforeEnter: requireAuth
    },
    {
      path: '/review',
      name: 'review',
      component: Review,
      beforeEnter: requireAuth
    },
    {
      path: '/review-info/:review_id',
      name: 'review-info',
      component: ReviewInfo,
      beforeEnter: requireAuth
    },
    {
      path: '*',
      name: '404',
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
