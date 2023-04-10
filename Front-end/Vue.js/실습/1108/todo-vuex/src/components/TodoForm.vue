<template>
  <div>
    <input 
      type="text"
      v-model.trim="message"
      @keyup.enter="upMessage"
    >
    <button @click="upMessage">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      message: null,
      isCompleted: false,
    }
  },
  methods: {
    upMessage(){
      if(this.message){
      this.$store.dispatch('upMessage', this.message)
      } else {
        alert('내용을 입력해주세요.')
      }
      this.message = null
    },
    
  },
  computed: {
    MData() {
      return this.$store.state.MData
    }
  }
}
</script>

<style>

</style>