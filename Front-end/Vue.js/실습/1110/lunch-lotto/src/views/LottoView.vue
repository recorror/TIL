<template>
  <div>
    <h1>{{menu}} 먹고 Lotto 추첨</h1>
    <button @click="pickNumbers">Pick Numbers</button>
    <div v-if="lottoNum">
      <p>{{lottoNum}}</p>
      <router-link :to="{name:'lunch'}">처음으로..</router-link>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
export default {
  name: 'LottoView',
  data(){
    return{
      lottoNum: null,
      menu: this.$route.params.menu
    }
  },
  methods: {
    pickNumbers(){
      const lottoNum = _.sortBy(_.sampleSize(_.range(1, 46), 6))
      this.lottoNum = lottoNum
    }
  }
}
</script>

<style>

</style>