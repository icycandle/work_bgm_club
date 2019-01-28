<template>
  <div class="music-detail">
    <h5 v-if="bgmId">來自{{username}}的{{jobType}}背景音樂 #{{bgmId}}</h5>
    <iframe
      v-if="youtubeLink"
      width="560"
      height="315"
      :src="youtubeLink"
      frameborder="0"
      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
    <br>
    {{comment}}
  </div>
</template>

<script>

export default {
  name: 'BackGroundMusicDetail',
  methods: {
    parseYouTubeHash(url) {
      const pattern1 = /youtube\.com\/watch\?v=(wjVjHce8uME)/;
      const pattern2 = /youtu\.be\/(wjVjHce8uME)/;
      if (url.match(pattern1)) {
        const regexResult = url.match(pattern1);
        const hash = regexResult[1];
        return hash;
      } else if (url.match(pattern2)) {
        const regexResult = url.match(pattern2);
        const hash = regexResult[1];
        return hash;
      }
      return false;
    },
  },
  created() {
    const vm = this;
    const bgmId = this.$route.params.id;
    const apiUrl = `/api/musiclinks/${bgmId}.json`;
    this.axios({
      url: apiUrl,
      method: 'GET',
    })
      .then((result) => {
        console.log(result);
        vm.url = result.data.url;
        vm.jobType = result.data.jobtype;
        vm.comment = result.data.comment;
        vm.username = result.data.username;
        vm.bgmId = result.data.id;
        const youtubeHash = vm.parseYouTubeHash(vm.url);
        vm.youtubeLink = `https://www.youtube.com/embed/${youtubeHash}`;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  data() {
    return {
      youtubeLink: '',
      jobType: '',
      bgmId: null,
      comment: '',
      username: '',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../scss/custom";

.music-detail {
  color: $main-color-light;
}
</style>
