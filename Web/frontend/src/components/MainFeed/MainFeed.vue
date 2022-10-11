<template>
  <div class="mainFeed">
    <Title/>
    <MakeTwit/>
    <Feed :updateFeed="updateFeed"/>
  </div>
</template>

<script>

import Title from "./Title";
import MakeTwit from "../MakeTwit/MakeTwit";
import Feed from "../Feed/Feed";
import {getAllFeed} from "../../api/feed";

export default {
  name: "MainFeed",
  components: {
    Title,
    MakeTwit,
    Feed
  },
  methods: {
    updateFeed(){
      this.$store.dispatch('feed/updateFeed', getAllFeed)
    }
  }
}
</script>

<style scoped>
.mainFeed {
  width: 55%;
  height: 100%;

  overflow: scroll;

  border: solid #e0e0e0 1px;
  border-top: none;
  border-bottom: none;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>