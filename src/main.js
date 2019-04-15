import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import config from './config'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import './filters'

var _hmt = _hmt || [];
window._hmt = _hmt; // 必须把_hmt挂载到window下，否则找不到
 (function () {
       var hm = document.createElement("script");
       hm.src = "https://hm.baidu.com/hm.js?"+ config.baidu_key;
       var s = document.getElementsByTagName("script")[0];
       s.parentNode.insertBefore(hm, s);
  })();

Vue.config.productionTip = false
Vue.use(ElementUI)

router.beforeEach((to, from, next) => {
    if (_hmt) {
        if (to.path) {
            _hmt.push(['_trackPageview', '/#' + to.fullPath]);
        }
    }
    next();
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
