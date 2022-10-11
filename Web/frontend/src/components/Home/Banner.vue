<template>
  <section class="logoContainer">
    <img :src="whiteLogo" alt="logo">
  </section>
</template>

<script>

import whiteLogo from '../../assets/whiteLogo.svg'

export default {
  name: "Banner",
  data() {
    return {
      whiteLogo
    }
  }
}
</script>

<style scoped>
.logoContainer {
  color: whitesmoke;
  background-image: url("https://simplyadtype.files.wordpress.com/2018/03/4ab3f660824505-5a5a6a9dde234.jpg");
  background-size: cover;

  width: 45%;

  display: flex;
  justify-content: center;
  align-content: center;
}

.logoContainer img {
  height: 40%;
  align-self: center;
}

</style>