<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="onlyData" @keyup.enter="saveAppData">
    <p>parentData: {{parentData[parentData.length-1]}}</p>
    <p>childData: {{childData[childData.length-1]}}</p>
    <AppParent
      :app-data="appData"
      @convey-child="conveyChild"
      @convey-parent="conveyParent"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'
export default {
  name: 'App',
  components: {
    AppParent,
  },
  data () {
    return {
      onlyData : '',
      appData : [],
      parentData : [],
      childData : [],
    }
  },
  methods: {
    saveAppData: function(){
      this.appData.push(this.onlyData)
    },
    conveyChild: function (cData) {
      this.childData.push(cData)
    },
    conveyParent: function (pData) {
      this.parentData.push(pData)
    }
  }
}
</script>

<style>
#app {
  border: solid 1px gray;
  text-align: center;
  /* border-bottom: 5; */
  width: 500px;
  margin: 100px auto;
}
</style>
