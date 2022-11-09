<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <OrderList/>
  </div>
</template>

<script>
import OrderList from '@/components/OrderList'
export default {
  name: 'App',
  components: {
    OrderList,
  },
  
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>