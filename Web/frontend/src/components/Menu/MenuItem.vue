<template>
  <li>
    <button @click="handleOnClick" :class="{active}" :id="activeId">
      <i :class="iClass" aria-hidden="true"></i>
      {{text}}
    </button>
  </li>
</template>

<script>
export default {
  name: "MenuItem",
  props:[
      'iClass',
      'text',
      'redirectTo',
      'active',
      "activeId"
  ],
  methods: {
    handleOnClick(){
      this.$router.push(this.redirectTo)
    }
  }
}
</script>

<style scoped>
button {
  display: flex;
  justify-content: space-between;

  background-color: inherit;
  border: none;
  border-radius: 20px;
  font-size: 1.5vw;

  padding: 5%;
  margin: 2%;
}

.actions nav button:hover {
  cursor: pointer;
  background-color: #e0e0e0;
}

.active {
  background-color: #41ABE1 !important;
  color: white !important;
}

i {
  font-size: 1.5vw;
  width: 20%;
}
</style>
