<template>
  <form class="music-form">
    <p class="alert alert-warning row" v-if="errors.length">
      <b>請修正下列錯誤:</b>
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </p>

    <div class="form-group row">
      <label class="col-sm-2 col-form-label" for="youtube-link">youtube 連結</label>
      <div class="col-sm-10">
        <input
          type="email"
          class="form-control"
          id="youtube-link"
          placeholder="https://youtu.be/xxxxxxxxx"
          v-model="youtubeLink"
        >
      </div>
    </div>
    <div class="form-group row">
      <label class="col-sm-2 col-form-label" for="jobtype">情境選擇</label>
      <div class="col-sm-10">
        <select class="form-control" id="jobtype" v-model="jobtype">
          <option
            v-for="option in options"
            :value="option"
            :key="option"
          >{{option}}</option>
        </select>
      </div>
    </div>
    <div class="form-group row">
      <label class="col-sm-2 col-form-label" for="comment">補充說明</label>
      <div class="col-sm-10">
        <textarea
          class="form-control"
          id="comment"
          rows="3"
          placeholder="(非必填)"
          v-model="comment"
        ></textarea>
      </div>
    </div>
    <div
    class="btn btn-primary btn-large"
    @click="checkForm"
    >送出表單，正式加入「工作背景音樂俱樂部」！</div>
  </form>
</template>

<script>
export default {
  name: 'MusicForm',
  methods: {
    checkYoutubeUrl(url) {
      if (!url) return false;
      const pattern1 = /www\.youtube\.com\/watch/;
      const pattern2 = /youtu\.be\//;
      if (url.match(pattern1)) {
        return true;
      } else if (url.match(pattern2)) {
        return true;
      }
      return false;
      // this.axios({
      //   url,
      //   method: 'GET',
      // })
      //   .then((result) => {
      //     console.log(result);
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    },
    checkForm() {
      this.errors = [];

      if (!this.checkYoutubeUrl(this.youtubeLink)) {
        this.errors.push('請確認輸入的 youtube 連結正確');
      }
      if (!this.jobtype) {
        this.errors.push('請選擇對應的工作情境');
      }

      if (!this.errors.length) {
        this.submit();
        return true;
      }
      return false;
    },
    submit() {
      const vm = this;
      const apiUrl = '/api/musiclinks';
      const postData = {
        url: this.youtubeLink,
        jobtype: this.jobtype,
        comment: this.comment,
      };

      this.axios({
        url: apiUrl,
        method: 'POST',
        data: postData,
      })
        .then((result) => {
          console.log(result);
          const bgmId = result.data.id;
          vm.$router.push({ name: 'music-detail', params: { id: bgmId } });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data: () => ({
    errors: [],
    youtubeLink: '',
    comment: '',
    jobtype: null,
    options: [
      '寫作業',
      '寫程式',
      '美術編輯',
      '文學創作',
      '行政業務',
      '沒有適合的類別 QwQ',
    ],
  }),
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../scss/custom";

.music-form {
  color: $main-color-light;
}
</style>
