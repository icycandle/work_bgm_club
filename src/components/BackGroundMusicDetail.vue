<template>
  <div class="music-detail pb-5">
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
    <br>
    <div class="row text-center justify-content-md-center">
      <a class="btn btn-primary col-3 mr-1" @click="userFeedbock(1)">
        <span v-if="feedBackValue===1" class="ccc"><span class="stdcolor">✓</span> 喜歡 ({{sumValue}})</span>
        <span v-else class="ccc">♥ 喜歡 ({{sumValue}})</span>
      </a>
      <a class="btn btn-primary col-3 mr-1" @click="userFeedbock(0)">
        <span v-if="feedBackValue===0" class="ccc"><span class="stdcolor">✓</span> 不喜歡</span>
        <span v-else class="ccc">✝ 不喜歡</span>
      </a>
      <a class="btn btn-primary col-3 mr-1" @click="userFeedbock(-1)">
        <span v-if="feedBackValue===-1" class="ccc"><span class="stdcolor">✓</span> 這不是音樂！</span>
        <span v-else class="ccc">⊘ 這不是音樂！</span>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BackGroundMusicDetail',
  methods: {
    parseYouTubeHash(url) {
      const pattern1 = /youtube\.com\/watch\?v=([-\d\w]+)/;
      const pattern2 = /youtu\.be\/([-\d\w]+)/;
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
    loadMusicData() {
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
          vm.sumValue = result.data.sum_value;
          vm.jobType = result.data.jobtype;
          vm.comment = result.data.comment;
          vm.username = result.data.username;
          const youtubeHash = vm.parseYouTubeHash(vm.url);
          vm.youtubeLink = `https://www.youtube.com/embed/${youtubeHash}`;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    loadUserFeedbock(value) {
      const vm = this;
      const apiUrl = `/api/musicrating?format=json&user=${window.currentUser}&musiclink=${vm.bgmId}`;
      this.axios({
        url: apiUrl,
        method: 'GET',
      })
        .then((result) => {
          if (result.data.count) {
            this.feedBackValue = result.data.results[0].value;
            this.feedBackId = result.data.results[0].id;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    userFeedbock(value) {
      const vm = this;
      let url;
      let method;
      if (this.feedBackValue === null) {
        url = '/api/musicrating.json';
        method = 'POST';
      } else {
        url = `/api/musicrating/${this.feedBackId}.json`;
        method = 'PATCH';
      }
      const data = {
        musiclink: this.bgmId,
        value,
      };
      this.axios({
        url,
        method,
        data,
      })
        .then((result) => {
          const valuediff = result.data.value - vm.feedBackValue;
          vm.feedBackValue = result.data.value;
          vm.sumValue += valuediff; // apply value to display
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.loadMusicData();
    this.loadUserFeedbock();
  },
  data() {
    return {
      youtubeLink: '',
      jobType: '',
      bgmId: this.$route.params.id,
      comment: '',
      username: '',
      feedBackValue: null,
      feedBackId: null,
      sumValue: null,
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
.ccc {
  color: $body-bg;
}
</style>
