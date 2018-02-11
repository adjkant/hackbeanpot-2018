<template>
  <div>
    <h1>Search</h1>
    <label for='company'>Company:</label>
    <input v-model="company" id="company">
    <br/>
    <label for='title'>Job Title:</label>
    <input v-model="title" id="title">
    <p>Search Now Button Here!</p>

    <p v-for="review in results">
      {{ review['job_type'] }}
    </p>

  </div>
</template>

<style scoped>

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