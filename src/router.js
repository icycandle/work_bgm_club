import VueRouter from 'vue-router';
import Vue from 'vue';

Vue.use(VueRouter);

const routes = [{
  path: '/',
  component: require('./components/Rules.vue').default,
},
{
  // this.$route.params.id
  path: '/bgm/:id',
  component: require('./components/BackGroundMusicDetail.vue').default,
},
{
  path: '/music-form',
  component: require('./components/MusicForm.vue').default,
},
{
  path: '/about-us',
  component: require('./components/AboutUs.vue').default,
},
  // {
  //     path: '/login',
  //     component: require('./components/Login.vue').default
  // },
  // {
  //     path: '/logout',
  //     component: require('./components/Logout.vue').default
  // },
];

export default new VueRouter({
  routes,
});
