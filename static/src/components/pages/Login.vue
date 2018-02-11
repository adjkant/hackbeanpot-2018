<template>
  <b-container class="fixed_center">
    <b-row align-v="center" class="justify-content-md-center">
        <b-card no-body class="text-center large_card round">
          <b-form class="login_form">
            <b-form-group id="login-email-group"
                          label="Email address"
                          label-for="login-email">
              <b-form-input id="login-email"
                            type="email"
                            v-model="login_email"
                            required
                            placeholder="Enter email"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-form-group id="login-password-group"
                          label="Password"
                          label-for="login-password">
              <b-form-input id="login-password"
                            type="password"
                            v-model="login_password"
                            required
                            placeholder="Enter password"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-btn class="submit_button" v-on:click="handleSubmit">Submit</b-btn>
          </b-form>
        </b-card>
    </b-row>
    <b-row align-v="end">
      <b-col align-self="end" class="no_account">
        Don't have an account? Click <router-link to="register" class="link">here</router-link> to make one!
      </b-col>
    </b-row>
  </b-container>
</template>

<style scoped>
  @import '~bootstrap/dist/css/bootstrap.css';
  @import '~bootstrap-vue/dist/bootstrap-vue.css';
  .round {
    border-radius: 10px;
  }
  .green_border {
    border-color: #38f8a6;
  }
  .submit_button {
    background-color: #19ab69;
    border-width: 0px;
  }
  .large_card {
    font-size: 1.5em;
    color: #333333;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    text-align: center;
  }
  .fixed_center {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .login_form {
    width: 500px;
    padding: 10% 20%;
  }
  .no_account {
    text-align: center;
    font-style: italic;
    color: #ffffff;
    font-size: 1.3em;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    margin-top: 10px;
    width: inherit;
  }
  .link {
    color: #ffffff;
    font-weight: bold;
    text-decoration: underline;
    text-decoration-color: #38f8a6;
  }
  .link:hover {
    color: #19ab69;
    text-decoration: underline;
    text-decoration-color: #ffffff;
  }

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

