<template>
  <section class="labels">
    <img :src="logo" alt="logo">
    <h1>В курсе<br/>происходящего</h1>
    <h2>Присоединяйтесь к Твиттеру прямо сейчас!</h2>
  </section>
</template>

<script>

import logo from '../../assets/logo.svg'

export default {
  name: "Labels",
  data(){
    return {
      logo
    }
  }
}
</script>

<style scoped>
.labels {
  height: 40%;
  margin-bottom: 3%;
}

.labels img {
  height: 15%;
}

.labels h1 {
  font-size: 3vw;
}

.labels h2 {
  font-size: 2.5vw;
}
</style>