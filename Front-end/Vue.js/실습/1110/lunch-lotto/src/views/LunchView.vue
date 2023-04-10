<template>
  <div>
    <h1>Lunch</h1>
    <button @click="randomMenu">Pick Lunch</button>
    <div v-if="menu">
      <p>{{menu}}</p>
      <button @click="goLotto">Lotto 뽑으러 가기</button>
    </div>
    <!-- 에밋 발생용 -->
    <button @click="sendData">Emit</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'LunchView',
  data(){
    return {
      menu: null,
    }
  },
  methods: {
    randomMenu(){
      const menuList = ['차돌짬뽕', '비빔냉면', '돼지국밥', '투움바 파스타']
      this.menu = _.sample(menuList)
    },
    goLotto(){
      this.$router.push({
        name: 'lotto',
        params: {
          menu: this.menu
        }
      })
    },
    sendData(){
      this.$emit('lunch-emit', this.mene)
    }
  },
}
</script>

<style>

</style>