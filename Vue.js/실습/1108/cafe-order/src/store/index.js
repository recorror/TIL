import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList:[],
    menuList:[{
      title: '아메리카노',
      price: 3000,
      selected: true, //초기값
      image: 'https://source.unsplash.com/featured/?americano'
    }],
    sizeList: [{
      name: 'small',
      price: 500,
      selected: true, //초기값
    }]
  },
  getters: {
  },
  mutations: {
    // addOrder(state) {
    //   orderList.push({menu: state.menuList[0], size: state.sizeList[0]})
    // },
    updateMenuList(state, selectedMenu) {
      state.menuList = state.menuList.map((se)=>{
        if (se === selectedMenu) {
          se.selected = !se.selected
        }
        return se
      })
    },
    updateSizeList(state, selectedSize) {
      state.sizeList = state.sizeList.map((se)=>{
        if(se === selectedSize) {
          se.selected = !se.selected
        }
        return se
      })
    },
  },
  actions: {
  },
  modules: {
  }
})
