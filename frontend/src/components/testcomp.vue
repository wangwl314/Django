<template>
<div>
  <button @click="showdata">showdata</button>
  <div>{{info}}</div>
</div>
</template>

<script>
import axios from "axios"
export default {
  name: "testcomp",
  data (){
    return {
      info: "$this.res"
    }
  },
  methods: {
    showdata (){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/apilogin/',
        headers: {Authorization: "489f25884854d624b7754e4b8364fb076917959f"},
      }).then(res => {
        console.log(res);
      })
    }
  },
}
</script>

<style scoped>

</style>