// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Cookies from 'js-cookie';
import App from './App';
import router from './router';

Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

const csrftoken = Cookies.get('csrftoken');
// Vue.http.headers.common.HTTP_X_CSRFTOKEN = csrftoken;
Vue.axios.defaults.headers.common = {
  'X-Requested-With': 'XMLHttpRequest',
  'X-CSRFToken': csrftoken,
};

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
