<template>
  <section class="actions">
    <img :src="logo" alt="logo">
    <nav>
      <ul>
        <MenuItem
            v-for="(item, index) in menuItems"
            v-bind:key="index"
            :iClass="item.iClass"
            :text="item.text"
            :redirectTo="item.redirectTo"
            :active="item.activeId === active"
            :activeId="item.activeId"
        />
      </ul>
    </nav>
  </section>
</template>

<script>

import logo from '../../assets/logo.svg'
import MenuItem from "./MenuItem";

export default {
  name: "MenuList",
  props: ['active'],
  data() {
    return {
      logo,
      menuItems: [
        {
          iClass: "fa fa-home",
          text: "Главная",
          redirectTo: "/feed",
          activeId: "feed"
        },
        {
          iClass: "fa fa-bell-o",
          text: "Уведомления",
          redirectTo: "/notification",
          activeId: "notification"
        },
        {
          iClass: "fa fa-user",
          text: "Профиль",
          redirectTo: "/profile",
          activeId: "profile"
        }
      ]
    }
  },
  components: {
    MenuItem
  }
}
</script>

<style scoped>
.actions {
  height: 50%;
  width: 90%;
}

.actions img {
  height: 7%;
  margin-left: 5%;
}

.actions nav ul {
  list-style: none;
  padding: 0;
}
</style>
