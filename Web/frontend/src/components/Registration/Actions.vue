<template>
  <button id="test_register" @click="handleRegisterClick">
    Зарегистрироваться
  </button>
</template>

<script>
export default {
  name: "Actions",
  props: ['handleRegister'],
  methods: {
    handleRegisterClick() {
      this.handleRegister()
          .then(() => this.$router.push('/feed'))
    }
  }
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
