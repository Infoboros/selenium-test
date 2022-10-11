<template>
  <div class="search">
    <SearchString/>
    <Footer/>
  </div>
</template>

<script>

import SearchString from "./SearchString";
import Footer from "./Footer";

export default {
  name: "Search",
  components: {
    SearchString,
    Footer
  }
}
</script>

<style scoped>
.search {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 25%;
  height: 97%;
  padding: 0 1%;
}
</style>