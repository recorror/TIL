<template>
  <div>
    <h1>My First Youtube Project</h1>
    <input 
      type="text"
      v-model="search"
      @keyup.enter="saveSearchKey"
    >
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SearchBar',
  data(){
    return {
      search: null,
    }
  },
  methods: {
    saveSearchKey() {
      const config = {
        params: {
          key: 'AIzaSyDuvPIf-TDC2fzov6I904vrJq32bB6vltA',
          part: 'snippet',
          type: 'video',
          q: this.search,
        }
      }
      axios.get('https://www.googleapis.com/youtube/v3/search', config)
        .then(response=>{
          // console.log(response.data.items)
          this.$store.commit('ITEMS', response.data.items)
        })
        .catch(error=>{
          console.log(error)
        })
      
    }
  }
}
</script>

<style>

</style>