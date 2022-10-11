<template>
  <section class="content">
    <slot/>
  </section>
</template>

<script>
export default {
  name: "Content"
}
</script>

<style scoped>
.content {
  height: 80%;

  display: flex;
  flex-direction: column;
}
</style>