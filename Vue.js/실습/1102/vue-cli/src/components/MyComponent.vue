<template>
  <div class="border">
    <h1>Create New Component made by me 프론트엔드</h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="naverUrl"
      @child-to-parent="pGetE"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem';
export default {
  name: 'MyComponent',
  components: {
    MyComponentItem,
  },
  data () {
    return {
      naverUrl: 'www.naver.com'
    }
  },
  methods: {
    pGetE: function(childData) {
      console.log('자식 컴포넌트에서 발생한 emit event 전달 받았다.')
      console.log(childData)
      this.$emit('asdf', childData)
    },
    getDynamicData: function (dynamicData) {
      console.log(`사용자가 입력한 값은 ${dynamicData}입니다.`)
    },
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>