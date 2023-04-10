  <template>
    <span>
      <MenuList/>
      <SizeList/>
    </span>  
  </template>
  
  <script>
  import MenuList from '@/components/MenuList'
  import SizeList from '@/components/SizeList'
  export default {
    name: 'OrderList',
    components: {
      MenuList,
      SizeList
    }
  }
  </script>
  
  <style>
  
  </style>