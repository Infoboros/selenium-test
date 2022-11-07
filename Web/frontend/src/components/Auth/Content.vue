<template>
  <section class="mainInfo">
    <h1>Чтобы приступить, введите свой адрес электронной почты и пароль.</h1>
    <form @submit.prevent="handleAuthClick()">
      <input id="test_username" type="email" placeholder="Адрес электронной почты" v-model="user.username">
    </form>
    <br>
    <form @submit.prevent="handleAuthClick()">
      <input id="test_password" type="password" placeholder="Пароль" v-model="user.password">
    </form>

    <h2 class="alert" v-if="badLogin">Указанные данные для авторизации неверные.</h2>
  </section>
</template>

<script>
export default {
  name: "Content",
  props: ['user', 'badLogin', 'handleAuthClick']
}
</script>

<style scoped>
.mainInfo {
  height: 100%;

  display: flex;
  flex-direction: column;
}

h1 {
  text-align: justify;
}

.alert {
  color: red;
  text-align: center;
}

form {
  height: 10%;
}

form input {
  width: 100%;
  height: 100%;

  font-size: 1em;
}
</style>
