<template>
  <section class="auth">
    <AuthButton text="Зарегистрироваться" :onClick="handleRegisterClick"/>
    <AuthButton text="Войти" :onClick="handleAuthClick"/>
  </section>
</template>

<script>

import AuthButton from "./AuthButton";

export default {
  name: "Auth",
  components: {
    AuthButton
  },
  methods: {
    handleAuthClick () {
      this.$router.push("/auth")
    },
    handleRegisterClick () {
      this.$router.push("/registration")
    }
  }
}
</script>

<style scoped>
.auth {
  display: flex;
  flex-direction: column;
  justify-content: start;
}
</style>