// Basics
import Vue from 'vue'
import Router from 'vue-router'

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
      component: Home
    },
    {
      path: '/profile',
      component: Profile
    },
    {
      path: '/profile/edit',
      component: ProfileEdit
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/company/:id',
      component: Company
    },
    {
      path: '/company/:id/:jobId',
      component: Company
    },
    {
      path: '/review',
      component: Review
    },
    {
      path: '*',
      component: Page404
    }
  ]
})
