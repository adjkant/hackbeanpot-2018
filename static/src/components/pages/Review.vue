<template>
  <div>
    <div v-show="stage == 1">
      <input v-model="company">
      <span v-on:click="nextStage">Select Company</span>
    </div>
    <div v-show="stage == 2">
      <span v-on:click="prevStage">Back</span>
      Position
      <input v-model="position">
      <span v-on:click="nextStage">Select Position</span>
    </div>
    <div class="ratings" v-if="stage == 3">

      <div class="progress">
        TODO
      </div>

      <div class="q_holder">
        <a>
          <div class="arrow prev" v-on:click="prevRating">
            <i class="fa fa-arrow-left" aria-hidden="true"></i>
          </div>
        </a>

        <div class="question">
          <h1>{{ question_cur["sec"] }}</h1>
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
    <div v-show="stage == 4">
      <span v-on:click="prevStage">Back to Ratings</span>
      <textarea v-model="review"></textarea>
      <span v-on:click="nextStage">Submit Review</span>
    </div>
    <div v-show="stage == 5">
      <span v-on:click="prevStage">Back to Review</span>
      Privacy
      <span v-on:click="nextStage">Submit Privacy</span>
    </div>
    <div v-show="stage == 6">
      <span v-on:click="prevStage">Go Back</span>
      Finalize
      <span v-on:click="submitReview">Finalize!</span>
    </div>
    <div v-show="stage == 7">
      Done!
    </div>
  </div>
</template>


<div class="med">{{ question_cur["med"] }}</div>

<style scoped>

  .ratings {
    margin: 0px 50px;
    background-color: green;
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
    padding-top: 250px;
    width: 10%;
    font-size: 60px;
    color: #90b0ff;
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
    background-color: #913a13;
    position: relative;
    height: 500px;
    width: 60%;
    max-width: 60%;
    vertical-align: middle;
  }

</style>

<script>

  import vueSlider from 'vue-slider-component';

  export default {
    name: '',
    components: {
      vueSlider
    },
    data: function() {
      return {
        company: '',
        position: '',
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
          sliderStyle: {
            "backgroundColor": "#f03d46"
          }
        },
        stage: 1,
        question_num: 0,
        question_cur: {
          sec: "A",
          q: "Question",
          low: "low low low low low low low low low low low",
          med: "med med med med med med med med med med med",
          high: "high high high high high high high high high high"
        },
        questions: [
          {
            sec: "A",
            q: "Question",
            low: "low low low low low low low low low low low",
            med: "med med med med med med med med med med med",
            high: "high high high high high high high high high high"
          },
          {
            sec: "A",
            q: "Question 2",
            low: "low 2",
            med: "med 2",
            high: "high 2"
          }
        ],
        answers: [50, 50]
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
        console.log('Will try to submit here');
      }
    }


  };



</script>

