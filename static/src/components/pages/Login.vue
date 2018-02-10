<template>
  <form>
    <br/>
    <label for="login-email">Email:</label>
    <input id="login-email" v-model="login_email">
    <br/>
    <label for="login-password">Password:</label>
    <input type="password" id='login-password' v-model="login_password">
    <br/>
    <div v-on:click="handleSubmit">Submit</div>
  </form>
</template>

<style scoped>

</style>

<script>

  import axios from 'axios';
  import router from '@/router/index';

  export default {
    name: 'login',
    data () {
      return {
        login_email: '',
        login_password: ''
      }
    },
    methods: {
      handleSubmit() {
        let instance = axios.create({
          baseURL: 'http://localhost:5000/api/'
        });

        let loginInfo = {
          email: this.login_email,
          password: this.login_password
        };

        instance.post('/user/login', loginInfo, { withCredentials: true })
          .then(response => {
            window.location = '/';
          })
          .catch(error => {
            this.login_password = '';
            this.login_email = '';
          });

      }
    }
  }

</script>

