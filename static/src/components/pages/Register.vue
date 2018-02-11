<template>
  <b-container class="fixed_center">
    <b-row align-v="center" class="justify-content-md-center">
        <b-card no-body class="text-center large_card round">
          <b-form class="register_form">
            <b-form-group id="first-group"
                          label="First name"
                          label-for="first">
              <b-form-input id="first"
                            type="text"
                            v-model="first"
                            required
                            placeholder="First name"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-form-group id="last-group"
                          label="Last name"
                          label-for="last">
              <b-form-input id="last"
                            type="text"
                            v-model="last"
                            required
                            placeholder="Last name"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-form-group id="email-group"
                          label="School Email Address"
                          label-for="email">
              <b-form-input id="email"
                            type="email"
                            v-model="email"
                            required
                            placeholder="smartyboi@harvard.edu"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-form-group id="school-group"
                          label="School"
                          label-for="school">
              <b-form-input id="school"
                            type="text"
                            v-model="school"
                            required
                            placeholder="Hogwarts"
                            class="green_border">
              </b-form-input>
            </b-form-group>
            <b-form-group id="password-group"
                          label="Password"
                          label-for="password">
              <b-form-input id="password"
                            type="password"
                            v-model="password"
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
      <b-col align-self="end" class="have_account">
        Already have an account? Click <router-link to="login" class="link">here</router-link> to log in!
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
    font-size: 1.3em;
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
  .register_form {
    width: 500px;
    padding: 10% 20%;
  }
  .have_account {
    text-align: center;
    font-style: italic;
    color: #ffffff;
    font-size: 1.2em;
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
  import axios from "axios";
  import router from "@/router/index";

  export default {
    name: "register",
    data () {
      return {
        error: null,
        first: "",
        last: "",
        email: "",
        school: "",
        password: "",
      }
    },
    methods: {
      handleSubmit() {
        let backend = axios.create({
          baseURL: "http://localhost:5000/api/"
        });

        let accountInfo = {
          first: this.first,
          last: this.last,
          email: this.email,
          password: this.password,
          school: this.school
        };

        console.log(accountInfo);

        backend.post("/user/create", accountInfo)
        .then(response => {
          this.doLogin(backend);
        })
        .catch(error => {
          this.error = true;
          console.log(error);
        });
      },
      doLogin(backend) {
        let loginInfo = {
          email: this.email,
          password: this.password,
        }
        backend.post('/user/login', loginInfo, {withCredentials: true})
        .then(response => {
          window.location = "/";
        })
        .catch(error => {
          this.error = true;
          console.log(error);
        })
      }
    }
  }
</script>

