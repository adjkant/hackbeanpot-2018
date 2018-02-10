<template>
  <div>
    <h1>404 Error Page Under Construction</h1>
    <h2>Path {{ $route.path.substr(1) }} not found</h2>
  </div>
</template>

<script>

export default {
  name: 'PageNotFound'
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
