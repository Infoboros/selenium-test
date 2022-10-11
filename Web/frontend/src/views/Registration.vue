<template>
  <main>
    <Modal>

      <template v-slot:content>
        <Content :badRegister="badRegister" :userData="userData" :handleRegister="handleRegister"/>
      </template>

      <template v-slot:actions>
        <Actions :handleRegister="handleRegister"/>
      </template>

    </Modal>
  </main>
</template>

<script>

import Modal from "../components/Modal/Modal";
import Content from '../components/Registration/Content'
import Actions from '../components/Registration/Actions'

export default {
  name: "Registration",
  components: {
    Modal,
    Content,
    Actions
  },
  data(){
    return {
      userData: {
        email: '',
        password: '',
        nick_name: '',
        id_name: ''
      },
       badRegister: false
    }
  },
  methods: {
    handleRegister(){
      this.$store.dispatch('auth/register', this.userData)
          .then(() => this.$router.push('/feed'))
          .catch(() => this.badRegister = true)
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