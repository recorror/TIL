import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    imgSrc : null,
  },
  getters: {
    catUrl (state) {
      return state.imgSrc
    }
  },
  mutations: {
    SAVE_CAT_IMG(state, data){
      state.imgSrc = data
    }
  },
  actions: {
    getCat(context){
      const catUrl = 'https://api.thecatapi.com/v1/images/search'
      axios.get(catUrl)
        .then((response) => {
          // console.log(response)
          // 데이터를 받아와서 저장한다.
          const catImg = response.data[0].url
          context.commit('SAVE_CAT_IMG', catImg)
        })
        .catch((error)=>{
          console.log(error)
        })
    }
  },
  modules: {
  }
})
