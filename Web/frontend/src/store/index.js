import Vue from 'vue'
import Vuex from 'vuex'
import AuthStore from './auth'
import UserStore from './user'
import FeedStore from './feed'
import EventsStore from './events'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth: AuthStore,
    user: UserStore,
    feed: FeedStore,
    events: EventsStore
  }
})
