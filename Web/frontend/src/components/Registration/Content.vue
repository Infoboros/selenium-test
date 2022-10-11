<template>
  <section class="mainInfo">
    <form @submit.prevent="handleRegister()">
      <h1>Создайте учетную запись</h1>
      <input name="firstName"  type="text" placeholder="Имя пользователя" v-model="userData.nick_name">
      <input name="secondName" type="text" placeholder="ID пользователя" v-model="userData.id_name">

      <h3>Данные для аутентификации</h3>
      <input name="login"  type="email" placeholder="Email" v-model="userData.email">
      <input name="password" type="password" placeholder="Пароль" v-model="userData.password">

      <h3 class="bad" v-if="badRegister">Возникла ошибка в ходе регистрации.</h3>
    </form>
  </section>
</template>

<script>
export default {
  name: "Content",
  props: ['badRegister', 'userData', 'handleRegister']
}
</script>

<style scoped>
h1 {
  font-size: 1.5em;
  margin: 0;
}

.bad {
  color: red;
}

.mainInfo {
  height: 50%;
}

.mainInfo form {
  display: flex;
  flex-direction: column;
  height: 80%;
}

.mainInfo form input {
  height: 25%;
  padding: 5px;
  margin-top: 5%;
  font-size: 1.5em;
}

.mainInfo form h1 {
  text-align: center;
}

.mainInfo form h3 {
  text-align: center;
  margin-top: 15%;
  margin-bottom: 0;
}
</style>