<template>
  <div class="profile">
    <Menu active="profile"/>
    <ProfileFeed/>
    <Search/>
  </div>

</template>

<script>

import Menu from "../components/Menu/Menu";
import ProfileFeed from "../components/Profile/ProfileFeed";
import Search from "../components/Search/Search";

export default {
  name: "Profile",
  components: {
    Menu,
    Search,
    ProfileFeed
  }
}
</script>

<style scoped>
.profile {
  height: 100%;
  width: 65%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>