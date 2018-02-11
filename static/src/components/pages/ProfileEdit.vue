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
                          label="Email Address"
                          label-for="email">
              <b-form-input id="email"
                            type="email"
                            v-model="email"
                            required
                            placeholder="smartyboi2@harvard.edu"
                            class="green_border">
              </b-form-input>
            </b-form-group>
    <b-btn class="submit_button" v-on:click="togglePass">{{buttonMsg}}</b-btn>
    <div v-if="showPass">

            <b-form-group id="password-group"
                          label="Password"
                          label-for="password">
              <b-form-input id="pass1"
                            type="password"
                            v-model="password1"
                            required
                            placeholder="New password"
                            class="green_border">
              </b-form-input>
              <b-form-input id="pass2"
                            type="password"
                            v-model="password2"
                            required
                            placeholder="Confirm password"
                            class="green_border">
              </b-form-input>
            </b-form-group>

          </div>
            <b-btn class="submit_button" v-on:click="submitEdit">Save Changes</b-btn>
          </b-form>
        
        </b-card>
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
    name: "profile-edit",
    data: function () {
        return {
          email: "",
          first: "",
          last: "",
          password1: "",
          password2: "",
          showPass: false,
          buttonMsg: "Change Password",
          backend: axios.create({baseURL: "http://localhost:5000/api/"})
        }
    },
    created: function () {
      this.backend.get("user/get", {withCredentials: true})
      .then(response => {
        console.log(response)
        this.email = response.data["email"];
        this.last = response.data["last"];
        this.first = response.data["first"];
        this.password1 = "";
        this.password2 = "";
      })
      .catch(error => {
        // TODO: Something
        console.log(error);
      })
    },
    methods: {
      submitEdit() {
        let editData = {
          email: this.email,
          first: this.first,
          last: this.last,
          first: this.first,
        }
        if (this.showPass) {
          if (this.password1 == this.password2){
            editData["password"] = this.password1;
          } else {
            // TODO: inform user somehow
            console.log("Passwords don't match!")
          }
        }
        console.log(editData)
        this.backend.put("user/edit", editData, {withCredentials: true})
        .then(response => {
          window.location = "/profile"
        })
        .catch(error => {
          // TODO:actually handle this error
          console.log(error)
        })
      },
      togglePass() {
        this.showPass = !this.showPass
        if (this.showPass) {
          this.buttonMsg = "Cancel";
        } else {
          this.buttonMsg = "Change Password";
        }
      }
    }
  };

</script>
