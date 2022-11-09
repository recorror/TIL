<template>
  <div>
    <img src="../assets/logo.png" alt="vueLogo">
    <HelloWorld
      :message=message
    />
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld'
export default {
  name: 'FirstView',
  data(){
    return{
      message: '첫 번째 페이지입니다.'
    }
  },
  components:{
    HelloWorld
  }
}
</script>

<style>

</style>