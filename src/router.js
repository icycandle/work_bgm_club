import VueRouter from 'vue-router';
import Vue from 'vue';

import Rules from './components/Rules';
import BackGroundMusicDetail from './components/BackGroundMusicDetail';
import MusicForm from './components/MusicForm';
import AboutUs from './components/AboutUs';

Vue.use(VueRouter);

const routes = [{
  path: '/',
  component: Rules,
},
{
  // this.$route.params.id
  path: '/bgm/:id',
  component: BackGroundMusicDetail,
},
{
  path: '/music-form',
  component: MusicForm,
},
{
  path: '/about-us',
  component: AboutUs,
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
