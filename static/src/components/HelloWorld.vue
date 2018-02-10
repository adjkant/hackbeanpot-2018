<template>
  <div class="hello">
    <h1>Hello Test</h1>
    <h2>Message from Backend: {{msg}}</h2>
  </div>
</template>

<script>
import axios from 'axios';

var instance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/'
});

export default {
  name: 'HelloWorld',
  data() {
    return {msg: ''};
  },

  created() {
    instance.get('test/test')
    .then(response => {
      this.msg = response.data;
    })
    .catch(response => {
      console.log(response);
    })

  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
