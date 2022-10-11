<template>
  <div class="modal">
    <Title/>

    <Content>
      <slot name="content"/>
    </Content>

    <Actions>
      <slot name="actions"/>
    </Actions>
  </div>
</template>

<script>

import Title from "./Title";
import Content from "./Content";
import Actions from "./Actions";

export default {
  name: "Modal",
  components: {
    Title,
    Content,
    Actions
  }
}
</script>

<style scoped>
.modal {
  height: 60%;
  width: 25%;
  padding: 1.5%;

  border-radius: 35px;
  background-color: #fff;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  align-self: center;
}
</style>