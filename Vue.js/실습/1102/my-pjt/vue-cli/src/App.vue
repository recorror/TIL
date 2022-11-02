<template>
  <div id="app">
    <TheLunch/>
    <TheLotto/>
  </div>
</template>

<script>
import TheLotto from '@/components/TheLotto';
import TheLunch from '@/components/TheLunch';

export default {
  name: 'App',
  components: {
    TheLotto,
    TheLunch,
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
