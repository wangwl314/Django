<template>
  
  <div>  
  <div style="margin-right:7%">  
    <navibar>
      <naviitem path='/'>首页</naviitem>
      <naviitem path='/tech'>技术</naviitem>
      <naviitem path='/other'>其他</naviitem>
      <naviitem path='/about' v-if="this.$store.state.loginstat">关于</naviitem> 
      <naviitem path='/login' v-if="!this.$store.state.loginstat">记录</naviitem> 
    </navibar>
  </div>  

    <div>
      <intro>
      <img  src='@/assets/img/logo.png'>
      <p>作者信息</p>
      </intro>
    </div>

  <div>
    <abstract></abstract>
  </div>
  
    <button @click="showdata" style="margin-left:90px;">test</button>

  </div>
</template>

<script>
  import navibar from '../components/navigate/navibar'
  import naviitem from '../components/navigate/naviitem'
  import intro from '../components/introduce/intro'
  import login from '../components/login/login'
  import abstract from '../components/abstract/abstract'
  import axios from 'axios'
  export default {
    name:'Home',
    methods:{
      showdata (){
        let x = this.$store.state.access
        let y = this.$store.state.refresh
        console.log(x, y);
      }
     },
     components:{
      intro,
      naviitem,
      navibar,
      login,
      abstract,
    }, 
  }
</script>


<style>
@import '../assets/css/base.css';
</style>

