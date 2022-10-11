<template>
  <div class="feed">
    <Menu active="feed"/>
    <MainFeed/>
    <Search/>
  </div>

</template>

<script>

import Menu from "../components/Menu/Menu";
import MainFeed from "../components/MainFeed/MainFeed";
import Search from "../components/Search/Search";

export default {
  name: "Feed",
  components: {
    Menu,
    MainFeed,
    Search
  }
}
</script>

<style scoped>
.feed {
  height: 100%;
  width: 65%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>