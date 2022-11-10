<template>
  <div id="app">
    <SearchBar/>
    <DetailView/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import DetailView from '@/components/DetailView'
export default {
  name: 'App',
  components: {
    SearchBar,
    DetailView
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
