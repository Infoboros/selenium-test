<template>
  <section class="auth">
    <AuthButton id="test_registration" text="Зарегистрироваться" :onClick="handleRegisterClick"/>
    <AuthButton id="test_login" text="Войти" :onClick="handleAuthClick"/>
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
