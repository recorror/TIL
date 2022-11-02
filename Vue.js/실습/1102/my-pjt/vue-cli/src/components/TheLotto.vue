<template>
  <div>
    <h2>로또</h2>
    <input type="button" value="Lotto Number">
    <p>{{random}}</p>
  </div>
</template>

<script>
export default {
  name: 'TheLotto',
  data () {
    return {
      lottoNum : []
    }
  },
  methods: {
    random() {
      this.lottoNum.push(this._.random(1,46))
      return this.lottoNum
    }
  }
}
</script>

<style>

</style>