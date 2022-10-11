<template>
<div class="menu">
  <MenuList :active="active"/>
  <Profile/>
</div>
</template>

<script>

import MenuList from "./MenuList";
import Profile from "./Profile";

export default {
  name: "Menu",
  props: ['active'],
  created() {
    this.$store.dispatch('user/update')
  },
  components: {
    MenuList,
    Profile
  }
}
</script>

<style scoped>
.menu {
  height: 95%;
  width: 20%;

  margin-right: 1%;


  display: flex;
  flex-direction: column;
  justify-content: space-between;

}
</style>