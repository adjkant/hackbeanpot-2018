<template>
  <div class="menu">
    <div class="title">Cooperate</div>
    <div class="icons">
      <span v-if="!$cookies.get('sessionToken')">
        <router-link to="/"><i class="fa fa-home" aria-hidden="true"></i></router-link>
        <router-link to="/login"><i class="fa fa-user" aria-hidden="true"></i></router-link>
      </span>

      <span v-if="$cookies.get('sessionToken')">
        <router-link to="/home"><i class="fa fa-home" aria-hidden="true"></i></router-link>
        <router-link to="/review"><i class="fa fa-plus-square-o" aria-hidden="true"></i></router-link>
        <router-link to="/search"><i class="fa fa-search" aria-hidden="true"></i></router-link>
        <router-link to="/profile"><i class="fa fa-user" aria-hidden="true"></i></router-link>
        <a href="#"><a v-on:click="logout"><i class="fa fa-sign-out" aria-hidden="true"></i></a></a>
      </span>
    </div>
  </div>
</template>

<style scoped>
  a {
    color: inherit;
    text-decoration: None;
  }
  .menu {
    display: inline-block;
    width: 100%;
    color: white;
    background-color: #fc5f45;
    height: 60px;
  }
  .title {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    font-size: 35px;
    font-weight: bold;
    font-style: italic;
    float: left;
    padding: 10px 20px;
  }
  .icons {
    float: right;
    padding: 0px 20px;
  }
  .fa {
    font-size: 30px;
    padding: 10px 15px;
  }


</style>

<script>
  import axios from 'axios';
  import router from '@/router/index';

  export default {
    name: 'site-menu',
    methods: {
      logout() {
        let instance = axios.create({
          baseURL: 'http://localhost:5000/api/'
        });

        instance.post('/user/logout', {}, {withCredentials: true})
          .then(response => {
            console.log('Logged out');
            window.location = '/';
          })
          .catch(error => {
            console.log(error);
            //window.location = '/';
          });
      }
    }
  };

</script>
