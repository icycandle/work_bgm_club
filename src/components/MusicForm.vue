<template>
  <form class="music-form"
    @submit="checkForm"
    method="post"
    >
    <p v-if="errors.length">
      <b>Please correct the following error(s):</b>
      <ul>
        <li v-for="error in errors">{{ error }}</li>
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
    <button type="submit" class="btn btn-primary btn-large">送出表單，正式加入「工作背景音樂俱樂部」！</button>
  </form>
</template>

<script>
export default {
  name: 'MusicForm',
  methods: {
    checkYoutubeUrl(url) {
      this.axios({
        url,
        method: 'GET',
      })
        .then((result) => {
          console.log(result);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    checkForm(e) {
      this.errors = [];

      if (this.youtubeLink !== 100) {
        this.errors.push('Total must be 100!');
      }

      if (!this.errors.length) {
        return true;
      }

      e.preventDefault();
      return false;
    },
    submit() {
      const apiUrl = '/api/musiclinks.json';
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
