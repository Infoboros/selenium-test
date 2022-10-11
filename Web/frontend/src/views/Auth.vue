<template>
  <main>
    <Modal>

      <template v-slot:content>
        <Content :user="user" :badLogin="badLogin" :handleAuthClick="handleAuthClick"/>
      </template>

      <template v-slot:actions>
        <Actions :handleAuthClick="handleAuthClick"/>
      </template>

    </Modal>
  </main>
</template>

<script>

import Modal from "../components/Modal/Modal";
import Actions from "../components/Auth/Actions";
import Content from "../components/Auth/Content";

export default {
  name: "Auth",
  components: {
    Modal,
    Actions,
    Content
  },
  data() {
    return {
      user: {
        username: 'e@e.e',
        password: 'e'
      },
      badLogin: false
    }
  },
  methods: {
    handleAuthClick() {
      this.$store.dispatch('auth/login', this.user)
          .then(() => this.$router.push('/feed'))
          .catch(() => this.badLogin = true)
    }
  }
}
</script>

<style scoped>
main {
  background-color: grey;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
}
</style>