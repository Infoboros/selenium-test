<template>
  <section class="title">
            <span class="close" @click="handleCloseClick">
                &#xd7;
            </span>
    <div class="imgContainer">
      <img :src="logo" alt="logo">
    </div>
  </section>
</template>

<script>

import logo from '../../assets/logo.svg'

export default {
  name: "Title",
  data () {
    return {
      logo
    }
  },
  methods:{
    handleCloseClick() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
.title {
  height: 5%;
  width: 100%;
  margin-bottom: 7%;

  display: flex;
}

.title .close {
  font-size: 32px;
}

.title .close:hover {
  color: grey;
  cursor: pointer;
}

.title .imgContainer {
  width: 100%;
  display: flex;
  justify-content: center;
}

.title .imgContainer img {
  height: 100%;
}

</style>