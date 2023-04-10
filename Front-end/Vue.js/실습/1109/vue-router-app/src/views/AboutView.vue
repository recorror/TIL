<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{name:'home'}">홈으로</router-link>
    <button @click="toHome">홈으로</button>
    <input 
      type="text"
      @keyup.enter="homeName"
      v-model="hName"
    >
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      hName : null,
    }
  },
  methods: {
    toHome(){
      this.$router.push({ name: 'home' })
    },
    homeName(){
      this.$router.push({ name: 'hello', params: { userName: this.hName } })
    }
  }
}
</script>