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
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background-color: #ececec;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    min-height: 100%;
  }
</style>
