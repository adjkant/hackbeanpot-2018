<template>
  <div>
    <div v-show="stage == 1" class="large_card fixed_center">
      <b-form class="login_form">
      Company
      <input v-model="review.company">
      Position
      <input v-model="review.position">
      City
      <input v-model="review.city">
      Duration
      <input v-model="review.duration">
      Salary
      <input v-model="review.salary"><br><br>
      <select v-model="review.job_type">
        <option value="co-op">Co-op</option>
        <option value="internship">Internship</option>
        <option value="reu">REU</option>
        <option value="remote">Remote</option>
      </select><br><br>
      <span v-on:click="nextStage">Start Review</span>
        </b-form>
    </div>

    <div class="ratings" v-if="stage == 2">

      <div class="q_holder">
        <a>
          <div class="arrow prev" v-on:click="prevRating">
            <i class="fa fa-arrow-left" aria-hidden="true"></i>
          </div>
        </a>

        <div class="question">
          <p>
            {{ question_cur["q"] }}
          </p>
          <span class="rat-slide"><vue-slider v-model="rat_value" v-bind="options"></vue-slider></span>
          <div>
            <div class="low">{{ question_cur["low"] }}</div>
            <div class="med">{{ question_cur["med"] }}</div>
            <div class="high"> {{ question_cur["high"] }}</div>
          </div>

        </div>

        <a>
          <div class="arrow next" v-on:click="nextRating">
            <i class="fa fa-arrow-right" aria-hidden="true"></i>
          </div>
        </a>
      </div>

    </div>
    <div v-show="stage == 3">
      <span v-on:click="prevStage">Back to Ratings</span>
      <textarea v-model="review.text"></textarea>
      <span v-on:click="nextStage">Submit Review</span>
    </div>
    <div v-show="stage == 4">
      <span v-on:click="prevStage">Back to Review</span>
      Privacy: Minimum People
      <input v-model="review.min_show">
      <span v-on:click="nextStage">Submit Privacy</span>
    </div>
    <div v-show="stage == 5">
      <span v-on:click="prevStage">Go Back</span>
      Finalize
      <span v-on:click="submitReview">Finalize!</span>
    </div>
    <div v-show="stage == 6">
      Done!
    </div>
  </div>
</template>


<div class="med">{{ question_cur["med"] }}</div>

<style scoped>
  @import '~bootstrap/dist/css/bootstrap.css';
  @import '~bootstrap-vue/dist/bootstrap-vue.css';
  .round {
    border-radius: 10px;
  }
  .green_border {
    border-color: #38f8a6;
  }
  .submit_button {
    background-color: #19ab69;
    border-width: 0px;
  }
  .large_card {
    font-size: 1.5em;
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
  .login_form {
    width: 500px;
    padding: 10% 20%;
  }
  .no_account {
    text-align: center;
    font-style: italic;
    color: #ffffff;
    font-size: 1.3em;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    margin-top: 10px;
    width: inherit;
  }
  .link {
    color: #ffffff;
    font-weight: bold;
    text-decoration: underline;
    text-decoration-color: #38f8a6;
  }
  .link:hover {
    color: #19ab69;
    text-decoration: underline;
    text-decoration-color: #ffffff;
  }


  .ratings {
    margin: 0px 50px;
    height: 80%;
  }

  .progress {
    width: 100%;
    height: 100px;
  }

  .q_holder {
    width: 100%;
    height: 20%;
    display: inline-block;
  }

  .rat-slide {
    margin: 0 auto;
  }

  a {
    color: inherit;
    text-decoration: None;
  }

  .arrow {
    padding-top: 100px;
    width: 10%;
    font-size: 60px;
    color: #000000;
  }

  .prev {
    align-items: center;
    float: left;
  }

  .next {
    float: left;
  }

  .low {
    float: left;
    width: 25%;
  }

  .med {
    float: left;
    width: 25%;
    margin-left: 12.5%;
    margin-right: 12.5%;
  }

  .high {
    float: right;
    width: 25%;
  }

  .question {
    float: left;
    margin: 0px;
    padding: 10px 50px;
    position: relative;
    height: 500px;
    width: 60%;
    max-width: 60%;
    vertical-align: middle;
    font-size: 20px;
  }

</style>

<script>
  import axios from 'axios';
  import vueSlider from 'vue-slider-component';

  let instance = axios.create({
    baseURL: 'http://localhost:5000/api/'
  });

  let premade_questions = [
    {
      sec: "Slider Statements Explanation",
      q: "The following series of statements are going to help us calculate a rating for your internship or co-op. Use the slider below to indicate your response. Are you ready?",
      low: "Not at all.",
      med: "I guess?",
      high: "Heck, yeah!"
    },
    {
      sec: "Culture",
      q: "The company culture made my work experience feel meaningful and I enjoyed coming to work.",
      low: "Nope. I dreaded going to work.",
      med: "It was fine but not notable.",
      high: "I loved my office environment."
    },
    {
      sec: "Inclusivity & Diversity",
      q: "I felt that the the company emphasized hiring a diversity of talent, and was inclusive to other people’s identities, not just my own.",
      low: "No, this wasn’t a diverse or inclusive environment.",
      med: "There was an effort to be diverse and inclusive",
      high: "They went above and beyond in their diversity and inclusion."
    },
    {
      sec: "Facilities & Equipment",
      q: "The facility, office and equipment at my office always met the standards I needed to be effective at my job.",
      low: "No, the building was basically falling apart.",
      med: "The facility and equipment were adequate but nothing special.",
      high: "Wow. I want to move into my office."
    },
    {
      sec: "Work Balance",
      q: "I had the right balance of work to do during my internship. I was never overworked, but I was also never left with nothing to do.",
      low: "I always had way too much or way too little work.",
      med: "I was twiddling my thumbs or working late nights from time to time.",
      high: "I always felt like I was contributing but I wasn’t overworked."
    },
    {
      sec: "Perks",
      q: "My company offered job perks that went beyond paying well.",
      low: "I might have collected some company swag. Or pens.",
      med: "There were one or two cool perks that were more valuable than just a t-shirt.",
      high: "I was so well taken care of by my company I felt like royalty."
    },
    {
      sec: "Opportunities",
      q: "Because of my position, I was able to gain valuable, new experiences. Opportunities were widely available and they opened doors for me.",
      low: "I didn’t gain any new opportunities in this position.",
      med: "I gained some new, valuable experiences.",
      high: "This position didn’t just open doors, it gave me the keys to unlock them."
    },
    {
      sec: "Mentorship",
      q: "My coworkers were able to help teach me new things, act as a mentor, and guide me as I grew in my position.",
      low: "Nope, I pretty much figured out everything myself.",
      med: "I had some guidance from my coworkers.",
      high: "I gained more from this position because of the mentorship I received."
    },
    {
      sec: "Leadership / Direction / Purpose",
      q: "I felt inspired by the leadership and direction of the company and that my work was a meaningful, purpose-driven contribution to those goals.",
      low: "I didn’t feel inspired by the leadership or company mission.",
      med: "The direction and purpose I was serving in the company felt valuable.",
      high: "I was inspired to come to work by the direction and leadership in the company."
    },
  ];

  export default {
    name: '',
    components: {
      vueSlider
    },
    created() {
      console.log("TODO Company and Review Load");
      instance.get('/company/all', { withCredentials: true })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
      instance.get('/review/select', { withCredentials: true })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    },
    data: function() {
      return {
        review: {
          company: 'a',
          position: 'b',
          city: 'c',
          job_type: 'internship',
          text: 'test',
          min_show: 1,
          duration: 2,
          salary: 5.5,
        },
        rat_value: 50,
        options: {
          width: "100%",
          height: 20,
          dotSize: 35,
          min: 0,
          max: 100,
          disabled: false,
          show: true,
          speed: 0.3,
          reverse: false,
          lazy: false,
          tooltip: "never",
          piecewise: false,
          bgStyle: {
              "backgroundColor": "#57f043"
          },
        },
        stage: 1,
        question_num: 0,
        question_cur: premade_questions[0],
        questions: premade_questions,
        answers: [50, 50, 50, 50, 50, 50, 50, 50, 50]
      }
    },
    methods: {
      nextRating() {
        if (this.question_num < this.questions.length - 1) {
          this.answers[this.question_num] = this.rat_value;
          this.question_num += 1;
          this.rat_value = this.answers[this.question_num];
          this.question_cur = this.questions[this.question_num];
        } else {
          this.stage += 1;
        }
      },
      prevRating() {
        if (this.question_num > 0) {
          this.answers[this.question_num] = this.rat_value;
          this.question_num -= 1;
          this.rat_value = this.answers[this.question_num];
          this.question_cur = this.questions[this.question_num];
        } else {
          this.stage -= 1;
        }
      },
      nextStage() {
        this.stage += 1;
      },
      prevStage() {
        this.stage -= 1;
      },

      submitReview() {
        let reviewJSON = {
          job_type: this.review.job_type,
          duration: this.review.duration,
          location: this.review.city,
          salary: this.review.salary,
          ratings: this.answers,
          title: this.review.position,
          company: this.review.company,
          min_visible: this.review.min_show,
          show_immediate: true,
          review_text: this.review.text
        };

        console.log(reviewJSON);

        instance.post('/review/create', reviewJSON, { withCredentials: true })
          .then(response => {
            this.results = response.data;
            this.stage += 1;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }


  };



</script>

