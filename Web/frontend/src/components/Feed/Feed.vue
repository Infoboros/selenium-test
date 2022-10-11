<template>
  <section class="listTwits">
    <Twit v-for="twit in feed" :twitData="twit" :like="like" :repost="repost" :key="twit.id"/>
  </section>
</template>

<script>

import Twit from "./Twit";
import {mapGetters} from "vuex";
import {like, repost} from "../../api/events";

export default {
  name: "Feed",
  props: ['updateFeed'],
  created() {
    this.updateFeed()
    this.$store.dispatch('auth/getUserId')
  },
  computed: {
    ...mapGetters({
      feed: 'feed/feed'
    })
  },
  components: {
    Twit
  },
  methods: {
    repost(twitId, userId){
      this.$store.dispatch('feed/makeEvent', {
        twitId,
        userId,
        make: repost,
        description: 'Репост'
      })
    },
    like(twitId, userId){
      this.$store.dispatch('feed/makeEvent', {
        twitId,
        userId,
        make: like,
        description: 'Лайк'
      })
    }
  }
}
</script>

<style scoped>
.listTwits {
  width: 100%;
}
</style>