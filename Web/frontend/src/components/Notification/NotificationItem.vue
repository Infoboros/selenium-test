<template>
  <div class="item">
    <i :class="iClass" aria-hidden="true"></i>

    <div class="content">
      <h2>
        {{title}}
      </h2>
      <h3>
        {{text}}
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationItem",
  props: [
      'iClass',
      'title',
      'text'
  ]
}
</script>

<style scoped>
.item {
  display: flex;
  flex-direction: row;
  align-items: center;

  padding: 2%;

  border: solid #e0e0e0 1px;
}

.item i {
  padding: 5%;
  color: purple;
  font-size: 2vw;
}

.item .content {
  padding: 0 5%;
}

.item .content h2 {
  font-size: 1.65vw;
  margin: 0;
}

.item .content h3 {
  font-size: 1.2vw;
  margin: 2% 0 0 0;
  text-align: justify;
  font-weight: normal;
}

</style>