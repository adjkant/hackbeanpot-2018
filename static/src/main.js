// Basics
import Vue from 'vue'
import App from './App'
import router from './router'

// Components
import Menu from './components/global/Menu.vue'
import Footer from './components/global/Footer.vue'
import ReviewCard from './components/global/ReviewCard.vue'

import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue);

Vue.component('site-menu', Menu);
Vue.component('site-footer', Footer);
Vue.component('review-card', ReviewCard)

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
