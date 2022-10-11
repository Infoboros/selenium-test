<template>
  <section class="content">
    <Labels/>
    <Auth/>
  </section>
</template>

<script>

import Labels from "./Labels";
import Auth from "./Auth";

export default {
  name: "Content",
  components: {
    Labels,
    Auth
  }
}
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 2.5%;
}
</style>