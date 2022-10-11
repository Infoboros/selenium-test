<template>
  <section class="actions">
    <slot/>
  </section>
</template>

<script>
export default {
  name: "Actions"
}
</script>

<style scoped>
.actions {
  height: 15%;
  width: 100%;

  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
</style>