<template>
  <div>
    <h2>점심메뉴</h2>
    <input type="button" value="Pick One">
    <p></p>
  </div>
</template>

<script>
export default {
  name: 'TheLunch',
  data () {
    return {
      luanch : ['자장면', '짬뽕', '만두', '탕수육', '라조기', '양장피', '팔보채']
    }
  },
  methods: {
    selectOne: function(){
      this.luanch._.element
    }
  }
}
</script>

<style>

</style>