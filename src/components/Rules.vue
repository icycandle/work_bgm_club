<template>
  <div class="rules">
    <ul>
      <li>俱樂部規則一
        <span class="stdcolor">★</span>不要談論背景音樂俱樂部。分享你引以為豪的工作音樂。
      </li>
      <li>俱樂部規則二
        <span class="stdcolor">★</span>不要談論背景音樂俱樂部。分享的工作音樂以youtube連結為形式，歌單亦可。
      </li>
      <li>俱樂部規則三
        <span class="stdcolor">★</span>你將會收到來自陌生人的歌單，陪伴你完成你的工作。
      </li>
    </ul>

    <a href></a>

    <div class="alert alert-primary">
      <blockquote class="blockquote">
        <p
          class="mb-0"
        >{{message}}</p>
        <footer class="blockquote-footer">2019年某個距離週末還有三天半的週二下午，
          <cite title="Source Title">臺灣青年詩人羅毓嘉</cite>
        </footer>
      </blockquote>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Rules',
  data: () => ({
    message: '真的好喜歡上班啊怎麼辦呢'.repeat(25),
  }),
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../scss/custom";

.rules {
  // margin: 0 50px;
  text-align: justify;
  color: $main-color-light;
}
</style>
