<template>
  <div class="home">
    <Main/>
    <Footer/>
  </div>
</template>

<script>

import Main from '../components/Home/Main'
import Footer from "../components/Home/Footer";

export default {
  name: 'Home',
  components: {
    Main,
    Footer
  }
}
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>