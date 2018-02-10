<template>
  <div class="menu">
    <div class="title">Intern Up</div>
    <div class="icons">
      <i class="fa fa-home" aria-hidden="true"></i>
      <i class="fa fa-info-circle" aria-hidden="true"></i>
      <i class="fa fa-search" aria-hidden="true"></i>
      <i class="fa fa-user" aria-hidden="true"></i>
    </div>
  </div>
</template>

<style scoped>
  .menu {
    display: inline-block;
    width: 100%;
    color: white;
    background-color: #fc5f45;
    height: 60px;
  }
  .title {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    font-size: 35px;
    font-weight: bold;
    float: left;
    padding: 10px 20px;
  }
  .icons {
    float: right;
    padding: 0px 20px;
  }
  .fa {
    font-size: 30px;
    padding: 10px 15px;
  }


</style>

<script>

  export default {
    name: 'site-menu'
  };

</script>
