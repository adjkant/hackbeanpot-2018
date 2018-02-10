<template>
  <div class="footer">
    <div class="icons">
      <i class="fa fa-twitter" aria-hidden="true"></i>
      <i class="fa fa-instagram" aria-hidden="true"></i>
      <i class="fa fa-snapchat" aria-hidden="true"></i>
      <i class="fa fa-linkedin" aria-hidden="true"></i>
    </div>
    <div class="footer-text">Uh-oh. Now you have to follow our social media accounts.</div>
  </div>
</template>

<style scoped>
  .footer {
    position: absolute;
    bottom : 0;
    margin-top : 40px;
    width: 100%;
    color: white;
    background-color: #fc5f45;
    height: 60px;
  }
  .footer-text {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    float: right;
    font-size: 16px;
    padding: 20px 10px;
  }
  .icons {
    position: relative;
    vertical-align: middle;
    float: right;
    padding: 0px 20px;
  }
  .fa {
    font-size: 20px;
    padding: 10px 15px;
  }

</style>

<script>

export default {
  name: 'site-footer'
};

</script>


