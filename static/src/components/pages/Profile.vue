<template>
  <div>
    <h1>Profile</h1>
    <h2>Welcome, {{first}} {{last}}</h2>
    Click <router-link to="profile/edit">here</router-link> to edit account details.
  </div>
</template>

<style scoped>

</style>

<script>
  import axios from "axios";
  import router from "@/router/index";

  export default {
    name: 'profile',
    data: function () {
      return {
        email: "",
        first: "",
        last: "",
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
  };

</script>
