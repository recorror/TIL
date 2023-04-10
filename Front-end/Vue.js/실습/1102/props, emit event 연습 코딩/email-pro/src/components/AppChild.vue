<template>
  <div id="appChild">
    <h1>AppChild</h1>
    <input 
      type="text"
      v-model="inputData"
      @keyup.enter="sChildData"
    >
    <p>appData: {{appData[appData.length-1]}}</p>
    <p>parentData: {{parentData[parentData.length-1]}}</p>
    <p>childData: {{childData[childData.length-1]}}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: Array,
    parentData: Array,
  },
  data () {
    return {
      inputData: '',
      childData: [],
    }
  },
  methods: {
    sChildData: function(){
      this.childData.push(this.inputData)
      this.$emit('convey-child', this.childData[this.childData.length-1])
    }
  }
}
</script>

<style>
 #appChild {
  border: solid 1px purple;
  margin: 1;
 }
</style>