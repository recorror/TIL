import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //장고의 데이터를 못 쓰기위해 임의로 3번째 글부터 쓰기 위해 적어줌.
    article_id: 3,
    articles: [{
      id: 1,
      title: 'title',
      content: 'content',
      createdAt: new Date().getTime(),
    },
    {
      id: 2,
      title: 'title2',
      content: 'content2',
      createdAt: new Date().getTime(),
  }],
  
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article){
      state.articles.push(article)
      state.article_id = state.article_id + 1
    },
    DELETE_ARTICLE(state, article_id){
      state.articles = state.articles.filter((article)=>{
        return !(article.id === article_id)
      })
    }
  },
  actions: {
    createArticle(context, payload){
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createAt: new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})
