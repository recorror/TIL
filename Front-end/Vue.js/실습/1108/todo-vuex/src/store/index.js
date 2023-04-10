import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    MData: [],
  },
  getters: {
    allMessages(state){
      return state.MData.length
    },
    completedMessage(state){
      const cm = state.MData.filter((data) => {
        return data.isCompleted == true
      })
      return cm.length
    },
    uncomMessage(state, getters){
      return getters.allMessages - getters.completedMessage
    },
  },
  mutations: {
    UP_MESSAGE(state, data){
      state.MData.push(data)
    },
    DELETE_MESSAGE(state, data){
      // console.log(idxData)
      const idx = state.MData.indexOf(data)
      state.MData.splice(idx, 1)
    },
    TOGGLE_MESSAGE(state, data){
      //배열 업데이트
      //map으로 해당 객체 isCompleted 토글시켜준 값 return
      state.MData = state.MData.map((mdata)=>{
        if (mdata === data) {
          mdata.isCompleted = !mdata.isCompleted
        }
        return mdata
      })
    }
  },
  actions: {
    upMessage(context, upload){
      const items = {
        title: upload,
        isCompleted: false,
      }
      context.commit('UP_MESSAGE', items)
    },
    deleteMassage(context, data){
      // console.log(index)
      context.commit('DELETE_MESSAGE', data)
    },
    toggleMessage(context, data){
      context.commit('TOGGLE_MESSAGE', data)
    },
  },
  modules: {
  }
})
