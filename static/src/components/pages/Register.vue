<template>
  <div>
    <h1 v-if="this.error !== null">Warning: {{error}}</h1>
    <br/>
    <form>
      <label for="first">First Name:</label>
      <input v-model="first" id="first" placeholder="First Name">
      <br/>
      <label for="last">Last Name:</label>
      <input v-model="last" id="last" placeholder="Last Name">
      <br/>
      <label for="email">Email:</label>
      <input v-model="email" id="email" placeholder="smartyboi@harvard.edu">
      <br/>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password">
      <br/>
      <a value="Submit" v-on:click="handleSubmit">Submit</a>
    </form>
  </div>
</template>

<style scoped>
  h1, h2 {
      font-weight: normal;
  }
  ul {
      list-style-type: none;
      padding:  0;
  }
  li {
      display: inline-block;
      margin: 0 10px;
  }
  a {
      color: #42b983;
  }
</style>

<script>
  import axios from "axios";
  import router from "@/router/index";

  export default {
    name: "login",
    data () {
      return {
        error: null,
        first: "",
        last: "",
        email: "",
        password: "",
        school_id: null,
      }
    },
    methods: {
      handleSubmit() {
        let backend = axios.create({
          baseURL: "http://localhost:5000/api/"
        });

        let email_ext = this.email.split("@")[1];

        backend.get("email-ext/find/" + email_ext)
        .then(response => {
            console.log('Email lookup:')
            console.log(response)
            this.school_id = response.data['school_id'];
            this.handleSignup(backend)
        })
        .catch(error => {
          this.error = true;
          console.log(error);
        })
      },
      handleSignup(backend) {
        let accountInfo = {
          first: this.first,
          last: this.last,
          email: this.email,
          password: this.password,
          school_id: this.school_id
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

