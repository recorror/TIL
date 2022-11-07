<template>
  <div id="app">
    <h1>TodoList</h1>
    <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
    <h2>완료된 todo 수: {{ completedTodosCount }}</h2>
    <h2>미완료 todo 수: {{ unCompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
    <!-- <button @click="loadTodos">Todo 불러오기</button> -->
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    allTodosCount(){
      return this.$store.getters.allTodosCount
    },
    completedTodosCount(){
      return this.$store.getters.completedTodosCount
    },
    unCompletedTodosCount(){
      return this.$store.getters.unCompletedTodosCount
    }
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
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
