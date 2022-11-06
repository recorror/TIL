<template>
  <div id="appParent">
    <h1>AppParent</h1>
    <input 
      type="text"
      v-model="pInputData"
      @keyup.enter="saveParentData"
    >
    <p>appData: {{appData[appData.length-1]}}</p>
    <p>childData: {{childData[childData.length-1]}}</p>
    <AppChild
      :app-data="appData"
      :parent-data="parentData"
      @convey-child="conveyChild"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'
export default {
  name: 'AppParent',
  components: {
    AppChild
  },
  props: {
    appData: Array,
  },
  data () {
    return {
      pInputData: '',
      parentData : [],
      childData : [],
    }
  },
  methods: {
    saveParentData: function () {
      this.parentData.push(this.pInputData)
      this.$emit('convey-parent', this.parentData[this.parentData.length-1])
    },
    conveyChild: function (event) {
      this.childData.push(event)
      this.$emit('convey-child', this.childData[this.childData.length-1])
    },
  }
}
</script>

<style>
 #appParent{
  border: solid 1px orange;
 }
</style>