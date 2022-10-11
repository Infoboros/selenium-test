<template>
  <main class="main">
    <Banner/>
    <Content/>
  </main>
</template>

<script>

import Banner from "./Banner";
import Content from "./Content";

export default {
  name: "Main",
  components: {
    Banner,
    Content
  }
}
</script>

<style scoped>
.main {
  display: flex;
  align-self: center;
  height: 90%;
  width: 100%;
}
</style>