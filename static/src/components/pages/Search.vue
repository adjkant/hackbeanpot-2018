<template>
  <div class="fixed_center large_card">

    <b-form class="login_form">
          <h3>Search Reviews</h3>
      <label for='company'>Company</label>
      <input v-model="company" id="company">
      <br/>
      <label for='title'>Job Title</label>
      <input v-model="title" id="title">
    <br><br>
    <p class="smaller_font">[[ search feature currently implemented on backend and design but not front YET ]]</p>
    <b-btn class="submit_button">Search</b-btn>
    </b-form>
<!-- 
    <p v-for="review in results">
      {{ review['job_type'] }}
    </p>
 -->
  </div>
</template>

<style scoped>
  @import '~bootstrap/dist/css/bootstrap.css';
  @import '~bootstrap-vue/dist/bootstrap-vue.css';
  .smaller_font {
    font-size: 18px;
  }
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
    width: 500px;
    font-size: 1.5em;
    color: #333333;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    text-align: center;
  }
  .login_form {
    width: 500px;
    padding: 10% 20%;
  }
  .fixed_center {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
</style>

<script>
  import axios from 'axios';

  export default {
    name: '',
    data: function() {
      return {
        results: 'None yet',
        company: '',
        title: '',
      }
    },
    created() {
      let instance = axios.create({
        baseURL: 'http://localhost:5000/api/'
      });

      instance.get('/review/select', { withCredentials: true })
        .then(response => {
          this.results = response.data;
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  };

</script>