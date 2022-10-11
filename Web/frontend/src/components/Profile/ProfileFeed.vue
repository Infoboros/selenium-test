<template>
 <div class="profileFeed">
   <Title/>
   <ProfileInfo/>
   <Feed :updateFeed="updateFeed"/>
 </div>
</template>

<script>

import Title from "./Title";
import ProfileInfo from "./ProfileInfo";
import Feed from "../Feed/Feed";
import {getProfileFeed} from "../../api/feed";

export default {
  name: "ProfileFeed",
  components: {
    Title,
    ProfileInfo,
    Feed
  },
  methods: {
    updateFeed(){
      this.$store.dispatch('feed/updateFeed', getProfileFeed)
    }
  }
}
</script>

<style scoped>
.profileFeed {
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