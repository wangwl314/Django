<template>
  <div class="abstract">
    <h2>{{msg}}</h2>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'abstract',
  data (){
    return {
      msg: 'abstract'
    }
  },
  methods: {
    function (){
      axios({
        url: 'http://127.0.0.1:8000/api/article/',
        method: 'get'
      }).then(res => {
        console.log(res);
      })
    }
  }
}
</script>

<style scoped>
.abstract {border: 1px solid gray; width: 53%; position: absolute;
right: 11%;top: 13%;text-align: justify;line-height: 1.2;}
</style>