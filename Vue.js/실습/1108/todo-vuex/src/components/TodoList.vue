<template>
  <div>
    <h1>Todo List</h1>
    <h2>All Messages : {{allMessages}}</h2>
    <h4>Completed Message : {{completedMessage}}</h4>
    <h4>Uncompleted Message : {{uncomMessage}}</h4>
    <TodoListItem
      v-for="(data, index) in MData"
      :key="index"
      :data="data"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
  name: 'TodoList',
  components: {
    TodoListItem
  },
  computed: {
    MData(){
      return this.$store.state.MData
    },
    allMessages(){
      return this.$store.getters.allMessages
    },
    completedMessage(){
      return this.$store.getters.completedMessage
    },
    uncomMessage(){
      return this.$store.getters.uncomMessage
    }
  }
}
</script>

<style>

</style>