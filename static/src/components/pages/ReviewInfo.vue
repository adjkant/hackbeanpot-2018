<template>
  <b-card>
    <b-button class="btn btn-warning btn-circle btn-xl">{{ avg_rating }} </b-button>
    <b-div>
      Job Type: {{ job_type }}
      <br/>
      Location: {{ location }}
      <br/>
      Company: {{ company }}
      <br/>
      Location: {{ location }}
      <br/>
      Position: {{ position }}
      <br/>
      <br/>
      Review:
      <br/>
      {{ review_text }}
      <br/>
    </b-div>
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
  import axios from 'axios';
  import router from '@/router/index';

  export default {
    name: 'review-info',
    data: function () {
      return {
        company: '',
        rating: '',
        job_type: '',
        position: '',
        circle_color: '',
        review_text: '',
        backend: axios.create({baseURL: "localhost:5000/api"})
      }
    },
    created: function () {
      this.backend.get('review/get/' + $router.params.review_id)
      .then(response => {
        this.company = response.data['company_id'];
        this.rating = response.data['avg_rating'];
        this.job_type = response.data['job_type'];
        this.position = reponse.data['job_id'];
        this.review_text = response.data['review_text'];
        this.lookupCompany()
        this.lookupJob()
      })
      .catch(error => {
        console.log(error);
      })
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
    },
    methods: {
      lookupJob() {
        this.backend.get('job/' + this.position)
        .then(response => {
          this.position = response.data['title'];
        })
        .create(error => {
          console.log(error)
        });
      },
      lookupCompany() {
        this.backend.get('company/' + this.company)
        .then(response => {
          this.company = response.data['name'];
        })
        .create(error => {
          console.log(error)
        });
      }
    },
  };
</script>
