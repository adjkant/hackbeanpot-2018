<template>
  <div id="app">
    <site-menu></site-menu>
    <router-view/>
    <site-footer></site-footer>
  </div>
</template>

<script>
  import Menu from "./components/global/Menu.vue"

  export default {
    name: 'app',
    components: {
      Menu
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
