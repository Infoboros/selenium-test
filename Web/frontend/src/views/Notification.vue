<template>
  <div class="notification">
    <Menu active="notification"/>
    <NotificationFeed/>
    <Search/>
  </div>

</template>

<script>

import Menu from "../components/Menu/Menu";
import Search from "../components/Search/Search";
import NotificationFeed from "../components/Notification/NotificationFeed";

export default {
  name: "Notification",
  components: {
    Menu,
    Search,
    NotificationFeed
  }
}
</script>

<style scoped>
.notification {
  height: 100%;
  width: 65%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>