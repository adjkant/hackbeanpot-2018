
<template>
<b-container class="large_card">
    <b-row>
      <b-col cols="4">
        Hello {{ first }} {{ last }}!
        <br>
        {{ school }}
      </b-col>
      <b-col cols="8">
        <b-card-group deck>
            <review-card v-for="(value, key) in reviews" v-bind:review="review" v-bind:value="value" v-bind:key="key"></review-card>
          </b-card-group>
      </b-col>

    </b-row>
  </b-container>
</template>

<style scoped>
  .large_card {
    font-size: 1.5em;
    color: #333333;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    text-align: center;
  }
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
        school: "",
        school_id: "",
        reviews: [],
        backend: axios.create({baseURL: "http://localhost:5000/api/"})
      }
    },
    created: function () {
      this.backend.get("user/get", {withCredentials: true})
      .then(response => {
        console.log(response);
        this.email = response.data["email"];
        this.last = response.data["last"];
        this.first = response.data["first"];
        this.school_id = response.data["school_id"];
        this.password1 = "";
        this.password2 = ""; 
        this.backend.get('school/' + this.school_id, {withCredentials: true})
        .then(response => {
          this.school = response.data['name'];
        })
        .catch(error => {
          console.log(error);
        });
      })
      .catch(error => {
        // TODO: Something
        console.log(error);
      });

      this.backend.get("user/reviews", {withCredentials: true})
      .then(response => {
        console.log(response);

        this.$set(this, 'reviews', response.data)
        console.log(this.reviews)
      })
      .catch(error => {
        // TODO: Something
        console.log(error);
      });
    },
  };

</script>
