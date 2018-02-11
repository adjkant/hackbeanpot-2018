<template>
  <form>
    <h1>Edit Profile</h1>
    <label for="email">Email:</label>
    <input v-model="email" id="email">
    <br/>
    <label for="first">First Name:</label>
    <input v-model="first" id="first">
    <br/>
    <label for="last">Last Name:</label>
    <input v-model="last" id="last">
    <br/>
    <div v-on:click="togglePass">{{buttonMsg}}</div>
    <div v-if="showPass">
      <label>New Password:</label>
      <input type="password" id="pass1" v-model="password1">
      <label>Confirm Password:</label>
      <input type="password" id="pass2" v-model="password2">
    </div>
    <div v-on:click="submitEdit">Submit</div>
  </form>
</template>

<style scoped>

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
