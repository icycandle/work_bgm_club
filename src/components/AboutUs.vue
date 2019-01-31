<template>
  <div class="aboutus">
    <ol>
      <li>這個地下社團似乎是由一個叫做
        <span class="stdcolor">HitSong</span> 的神秘組織運營的。
      </li>
      <li>據傳，
        <span class="stdcolor">HitSong</span> 的組成分子是一群喜愛音樂的玩家與遊戲設計者。
      </li>
      <li>
        <span class="stdcolor">HitSong</span> 的終極計畫是，將音樂的樂趣重新植入人們的生活之中。他們是如此狂熱，簡直不擇手段。
      </li>
      <li>要找到
        <span class="stdcolor">HitSong</span> 的真身很困難，但你可以寄電子郵件到
        <email>service@dwave.cc</email>
        。
      </li>
      <li>其實
        <span class="stdcolor">HitSong</span> 根本就很喜歡閱讀大家寫來的電子郵件。
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'AboutUs',
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../scss/custom";

.aboutus {
  text-align: justify;
  color: $main-color-light;
}
</style>
