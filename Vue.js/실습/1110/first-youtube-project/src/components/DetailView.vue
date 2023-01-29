<template>
  <div v-if="search_url">
    <iframe 
      id="player" 
      type="text/html" 
      width="640" 
      height="360"
      :src="`http://www.youtube.com/embed/${search_url}`"
      frameborder="0">
    </iframe>
    <p>DETAil</p>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  computed: {
    search_url(){
      const result = this.$store.state.items[0].id.videoId
      if (result) {
        console.log(result)
        }
      return result
    }
  }
}
</script>

<style>

</style>