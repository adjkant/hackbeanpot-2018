<template>
  <form>
    <br/>
    <label for="login-email">Email:</label>
    <input id="login-email" v-model="login_email">
    <br/>
    <label for="login-password">Password:</label>
    <input type="password" id='login-password' v-model="login_password">
    <br/>
    <button value="Submit" v-on:click="handleSubmit">Submit</button>
  </form>
</template>

<style scoped>

</style>

<script>

  import axios from 'axios';

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

        console.log(loginInfo);

        instance.post('/user/login', loginInfo, {withCredentials: true})
          .then(response => {
            console.log('Got: ' + response.data);
            console.log(response.headers);
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }

</script>

