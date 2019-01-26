<template>
  <div class="music-detail">
    <h5>{{workType}} BGM #{{bgmId}}</h5>
    <iframe
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
  data() {
    const bgmId = 13;
    const youtubeHash = 'YSMXbbw2B8Y';
    const workType = '寫程式';
    const youtubeLink = `https://www.youtube.com/embed/${youtubeHash}`;
    const comment = 'lorem ipsem';
    return {
      youtubeLink,
      workType,
      bgmId,
      comment,
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
