<template>
  <div class="title">
    <h2>Главная</h2>
    <button class="popular">
      <i class="fa fa-star-o" aria-hidden="true"></i>
    </button>
  </div>
</template>

<script>
export default {
  name: "Title"
}
</script>

<style scoped>
.title {
  display: flex;
  justify-content: space-between;
  align-items: center;

  width: 95%;

  font-size: 1vw;
}

.title button {
  border: none;
  border-radius: 50px;

  font-size: 1.5vw;
  background-color: #fff;

  height: 1.5em;
}

.title button:hover {
  cursor: pointer;
  background-color: #e8e8e8;
}
</style>