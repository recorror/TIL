import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items:null,
  },
  getters: {
  },
  mutations: {
    ITEMS(state, payload) {
      state.items = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
