<template>
  <div>
    <span @click="toggleMessage()" :class="{'text-plus' : data.isCompleted}">
        {{data.title}}
      </span>
      <input 
        @click="deleteMessage()"
        type="button"
        value="Delete"
      >
  </div>
</template>

<script>
export default {
  name:'TodoListItem',
  props: {
    data:Object,
  },
  methods: {
    deleteMessage() {
      this.$store.dispatch('deleteMassage', this.data)
    },
    toggleMessage(){
      this.$store.dispatch('toggleMessage', this.data)
    }
  }
}
</script>

<style>
.text-plus {  
  text-decoration: line-through;
}
</style>