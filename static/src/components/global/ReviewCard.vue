<template>
  <b-media right-align slot="aside" width="80" vertical-align="center">
    <svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" v-bind:fill="circle_color" />
  <text x="50%" y="50%" font-size="2em" stroke="#51c5cf" stroke-width="0px" dy=".15em" text-anchor="middle" alignment-baseline="middle"> {{ rating }} </text>
</svg>
    <h5 class="mt-0 mb-1">{{ company }}</h5>
    {{ job_type }}
    {{ job_title }}
  </b-media>
</template>


<style scoped>
</style>

<script>
  export default {
    name: 'review-card',
    props: [
      'company',
      'rating',
      'job_type',
      'job_title',
    ],
    created: function () {
      this.circle_color = "#ffffff";
      switch(true) {
        case rating >= 9.0:
          this.circle_color = "green";
          break;
        case rating >= 8.0:
          this.circle_color = "";
          break;
        case rating >= 7.0:
          this.circle_color = "";
          break;
        default:
          this.circle_color = "#CCCCCC"
      }
    }
  };
</script>