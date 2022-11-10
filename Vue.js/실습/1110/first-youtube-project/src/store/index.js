import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items:null,
  },
  getters: {
    useItems(state){
      console.log(state.items)
      return state.items
    }
  },
  mutations: {
    ITEMS(state, data){
      state.items = data
    }
  },
  actions: {
  },
  modules: {
  }
})
