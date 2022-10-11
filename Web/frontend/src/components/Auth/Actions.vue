<template>
  <button @click="handleAuthClick">
    Войти
  </button>
</template>

<script>
export default {
  name: "Actions",
  props: ['handleAuthClick'],
}
</script>

<style scoped>
button {
  width: 100%;
  padding: 2%;

  color: #41ABE1;
  background-color: #fff;

  border: none;
  border-radius: 25px;

  font-size: 1em;
  font-weight: bold;
}

button:hover {
  cursor: pointer;

  background-color: rgba(65, 171, 225, 0.2);
}
</style>