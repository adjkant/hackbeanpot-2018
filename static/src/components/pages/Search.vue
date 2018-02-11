<template>
  <div>
    <h1>Search</h1>
    <label for='company'>Company:</label>
    <input v-model="company" id="company">
    <br/>
    <label for='title'>Job Title:</label>
    <input v-model="title" id="title">
    <p>Search Now Button Here!</p>
    <p>{{ results }}</p>
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


+import axios from 'axios';
+var instance = axios.create({
+  baseURL: 'http://127.0.0.1:5000/api/',
+  timeout: 1000,
+});
+
+export default {
+  name: 'HelloWorld',
+  data() {
+    return {msg: ''};
+  },
+
+  created() {
+    instance.get('test/test')
+    .then(response => {
+      this.msg = response.data;
+    })
+    .error(response => {
+      console.log(response);
+    })
+
+  }
