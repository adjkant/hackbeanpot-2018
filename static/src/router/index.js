import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Page404 from '@/components/Page404'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component: HelloWorld
    },
    {
      path: '/about',
      component: HelloWorld
    },
    {
      path: '/login',
      component: HelloWorld
    },
    {
      path: '/register',
      component: HelloWorld
    },
    {
      path: '/home',
      component: HelloWorld
    },
    {
      path: '/profile',
      component: HelloWorld
    },
    {
      path: '/profile/edit',
      component: HelloWorld
    },
    {
      path: '/search',
      component: HelloWorld
    },
    {
      path: '/company/:id',
      component: HelloWorld
    },
    {
      path: '/company/:id/:jobId',
      component: HelloWorld
    },
    {
      path: '/review',
      component: HelloWorld
    },
    {
      path: '*',
      component: Page404
    }
  ]
})
