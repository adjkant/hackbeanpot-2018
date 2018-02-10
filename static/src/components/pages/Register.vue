<template>
  <form>
      <label for='fName'>First Name:</label>
      <input v-model="fName" id="fName" placeholder="First Name">
      <br/>
      <label for='lName'>Last Name:</label>
      <input v-model="lName" id="lName" placeholder="Last Name">
      <br/>
      <label for='uName'>Username:</label>
      <input v-model="uName" id="uName" placeholder="Username">
      <br/>
      <label for='pWord'>Password:</label>
      <input type="password" id='pWord' v-model="pWord">
      <br/>
      <button value="Submit" v-on:click="handleSubmit">Submit</button>
  </form>
</template>

<style scoped>
  h1, h2 {
      font-weight: normal;
  }
  ul {
      list-style-type: none;
      padding:  0;
  }
  li {
      display: inline-block;
      margin: 0 10px;
  }
  a {
      color: #42b983;
  }
</style>

<script>
  import axios from 'axios';

  export default {
    name: 'login',
    data () {
      return {
        fName: '',
        lName: '',
        uName: '',
        pWord: '',
      }
    },
    methods: {
      handleSubmit() {
        let instance = axios.create({
          baseURL: 'http://localhost:5000/api/'
        });

        let loginInfo = {
          firstName: this.fName.value,
          lastName: this.lName.value,
          username: this.uName.value,
          password: this.pWord.value,
        };

        console.log(loginInfo);

        instance.post('/user/create',
                      loginInfo)
        .then(response => {
          console.log('Got: ' + response.data);
        })
        .catch(error => {
          console.log(error);
        });
      }
    }
  }
</script>

