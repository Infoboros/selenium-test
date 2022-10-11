<template>
  <div class="searchString">
    <form method="post">
      <label>
        <i class="fa fa-search" aria-hidden="true"></i>
        <input type="text" placeholder="Поиск в Твиттере">
      </label>
    </form>
  </div>
</template>

<script>
export default {
  name: "SearchString"
}
</script>

<style scoped>
.searchString {
  height: 3.5%;
  padding: 5%;
  border-radius: 50px;

  background-color: #e8e8e8;
}

.searchString form {
  height: 100%;
}

.searchString input {
  height: 100%;
  font-size: 1vw;

  border: none;
  background-color: inherit;
}
</style>