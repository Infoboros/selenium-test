<template>
  <button @click="onClick">
    {{text}}
  </button>
</template>

<script>
export default {
  name: "AuthButton",
  props: [
      'text',
      'onClick'
  ]
}
</script>

<style scoped>
button {
  display: flex;
  align-self: start;
  justify-content: space-evenly;
  align-items: center;
  min-width: 65%;

  margin: 1.5% 0;
  padding: 0.9% 2%;
  border-radius: 25px;
  background-color: #fff;
  height: 2.5vw;

  font-size: 1.5vw;
  white-space: nowrap;
  font-weight: bold;

  transition: 0.5s;
}

button:hover {
  cursor: pointer;
  border-color: #41ABE1;
  background-color: #41ABE1;
}

</style>