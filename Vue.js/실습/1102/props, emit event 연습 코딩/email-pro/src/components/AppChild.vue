<template>
  <div id="appChild">
    <h1>AppChild</h1>
    <input 
      type="text"
      v-model="inputData"
      @keyup.enter="sChildData"
    >
    <p>appData: {{appData[0]}}</p>
    <p>parentData: {{parentData[0]}}</p>
    <p>childData: {{childData[0]}}</p>
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
      this.$emit('convey-child', this.childData[0])
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