import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Couplet from './views/Couplet'
import Poem from './views/Poem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/couplet',
      name: 'couplet',
      component: Couplet
    },
    {
      path: '/poem',
      name: 'poem',
      component: Poem
    }
  ]
})
