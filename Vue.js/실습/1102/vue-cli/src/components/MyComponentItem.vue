<template>
  <div>
    <h3>this component in MyComponent</h3>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
    <button @click="cToP">클릭!</button>
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>

export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data : function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    cToP: function () {
      this.$emit('child-to-parent', '자식 컴포넌트에서 발생한 데이터다.')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null
    }
  },
}
</script>

<style>

</style>