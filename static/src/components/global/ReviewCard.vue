<template>
  <b-card>
    <router-link :to="review-info/value.id"<b-button class="btn btn-warning btn-circle btn-xl">{{ value.avg_rating }} </b-button></router-link>
    <br/>
    {{ company_name }}
    <br/>
    {{ value.job_type }}
    <br/>
    {{ value.location }}
</b-card>
</template>


<style scoped>
@import '~bootstrap/dist/css/bootstrap.css';
@import '~bootstrap-vue/dist/bootstrap-vue.css';

.rating_circle {
  color: black;
}

.btn-circle.btn-xl {
    width: 70px;
    height: 70px;
    padding: 10px 16px;
    border-radius: 35px;
    font-size: 24px;
    line-height: 1.33;
}

.btn-circle {
    width: 30px;
    height: 30px;
    padding: 6px 0px;
    border-radius: 15px;
    text-align: center;
    font-size: 12px;
    line-height: 1.42857;
}

</style>

<script>
  import router from "@/router/index";
  import axios from 'axios';
  export default {
    name: 'review-card', 
    data: function () {
      return {
        backend: axios.create({baseURL: "http://localhost:5000/api"}),
        company_name: '',
      }
    },
    props: [
      'company',
      'rating',
      'jtype',
      'jtitle',
      'reviewobj',
      'key',
      'value',
      'review'
    ],
    created: function () {
      this.backend.get('company/' + this.value.company_id, {withCredentials: true})
      .then(response => {
        this.company_name = response.data['name'];
      })
      .catch(error => {
        console.log(error);
      })
      this.circle_color = "#ffffff";
      switch(true) {
        case this.value.avg_rating >= 9.0:
          this.circle_color = "green";
          break;
        case this.value.avg_rating >= 8.0:
          this.circle_color = "";
          break;
        case this.value.avg_rating >= 7.0:
          this.circle_color = "";
          break;
        default:
          this.circle_color = "#CCCCCC"
      }
    }
  };
</script>
