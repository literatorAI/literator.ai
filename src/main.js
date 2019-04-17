import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import config from './config'

import ba from 'vue-ba'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

import './filters'

Vue.use(ba, config.baiduKey)

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(mavonEditor)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
