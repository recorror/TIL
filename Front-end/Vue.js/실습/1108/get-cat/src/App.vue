<template>
  <div id="app">
    <hr>
    <h1>Cat Image</h1>
    <button @click="getCat">Get Cat</button>
    <div v-show="catUrl">
      <img :src="catUrl" alt="cat image">
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  methods: {
    getCat(){
      this.$store.dispatch('getCat')
    },
  },
  computed: {
    catUrl(){
      return this.$store.getters.catUrl
    }       
  },
  created(){
    this.getCat()
  },
  updated(){
    console.log('이미지 리소스가 업데이트 되었습니다.')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
