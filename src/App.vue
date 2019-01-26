<template>
  <div id="app" class="container">
    <img alt="Vue logo" src="./assets/hitsong-doll.png" style="height:144px; width: 150px;">
    <h1 class="main-info" >WORK<span class="stdcolor">★</span>BGM CLUB</h1>
    <p class="main-info" >工作<span class="stdcolor">★</span>背景音樂俱樂部</p>
    <router-link to="/">rules<span class="stdcolor">★</span>規則</router-link>
    -
    <router-link to="/music-form">form<span class="stdcolor">★</span>送出歌單</router-link>
    -
    <router-link to="/about-us">about<span class="stdcolor">★</span>關於這裡</router-link>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
};
</script>

<style lang="scss">
@import './scss/custom';

#app {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 10px;
  color: $main-color-light;

  >h1.main-info {
    margin: 0;
  }
  .main-info {
    color: $main-color;
  }

  .stdcolor{
    color: $auxiliary-color;
  }

  >h1 {
    font-size: 400%;
  }
}
</style>
