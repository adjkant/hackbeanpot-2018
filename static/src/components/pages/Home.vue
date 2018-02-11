<template>
  <div class="fixed_center large_card">
    <h1>Hello!</h1>
    <p>Co-ops and internships are great. Super cool. They give students a chance to practice in their field, take advantage of increasingly competitive perks, and open doors to full-time jobs.</p>

    <p>But it’s not always clear what you’re getting into when you accept an offer. Jobs don’t always match their descriptions, interns get stuck doing more coffee runs than meaningful work, and students end up being overworked because they’re cheap or free labor.</p>

    <p>We wanted to make this process a little more clear, and provide students the opportunity to give honest feedback to each other about their co-op and internship positions. We develop our ratings based on responses on eight categories: culture, inclusivity, facilities, work balance, perks, opportunities, mentorship and purpose.</p>

    <p>Privacy is key to this process. Users remain anonymous, and reviews aren’t posted until a minimum number of reviews (set by the user) become available.</p>

    <p>So go out there! Gain experience! Just don’t forget to share your insights when you return.</p>
    <span v-if="!$cookies.get('sessionToken')">
      <router-link to="register"><b-btn to="register">Sign Up</b-btn></router-link>
      <router-link to="login"><b-btn class="submit_button" to="login">Log In</b-btn></router-link>
    </span>
  </div>
</template>

<style scoped>

  @import '~bootstrap/dist/css/bootstrap.css';
  @import '~bootstrap-vue/dist/bootstrap-vue.css';

  a a:visited a:hover {
    color: inherit;
  }

  .large_card {
    font-size: 1.5em;
    color: #333333;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    text-align: center;
  }
  .large_card_arrows {
    font-size: 1.5em;
    width: 80%;
    color: #333333;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    text-align: center;
  }
  .fixed_center {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .submit_button {
    background-color: #19ab69;
    border-width: 0px;
  }

  p {
    font-size: 18px;
  }

</style>



<script>

  export default {
    name: ''
  };

</script>

