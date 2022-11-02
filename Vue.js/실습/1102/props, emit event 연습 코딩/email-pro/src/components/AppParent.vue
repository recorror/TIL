<template>
  <div id="appParent">
    <h1>AppParent</h1>
    <input 
      type="text"
      v-model="pInputData"
      @keyup.enter="saveParentData"
    >
    <p>appData: {{appData[0]}}</p>
    <p>childData: {{childData[0]}}</p>
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
      this.$emit('convey-parent', this.parentData[0])
    },
    conveyChild: function (childData) {
      this.childData.push(childData)
      this.$emit('convey-child', this.childData[0])
    },
  }
}
</script>

<style>
 #appParent{
  border: solid 1px orange;
 }
</style>