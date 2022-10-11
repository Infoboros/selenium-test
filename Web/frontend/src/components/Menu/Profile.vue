<template>
  <section class="profile" @click="handleOnClick">
    <img :src="userData.avatar" alt="avatar" class="avatar">
    <div class="name">
      <h3>
        {{ userData.nick_name}}
      </h3>
      <span>
        @{{userData.id_name}}
      </span>
    </div>
    <button>
      <i class="fa fa-ellipsis-h" aria-hidden="true"></i>
    </button>
  </section>
</template>

<script>

import {mapGetters} from "vuex";

export default {
  name: "Profile",
  computed: {
    ...mapGetters('user', ['userData'])
  },
  methods: {
    handleOnClick() {
      this.$router.push('/profile')
    }
  }
}
</script>

<style scoped>
.avatar {
  border-radius: 100%;
  height: 5vh;
  width: 5vh;
}
.menu .profile {
  height: 4%;
  width: 95%;
  font-size: 1vw;
  padding: 5%;

  display: flex;
  justify-content: space-between;
}

.profile:hover {
  background-color: #e0e0e0;
  border-radius: 50px;
  cursor: pointer;
}

.profile .name  h3 {
  margin: 0;
}

.profile .name  h4 {
  color: #a2a2a2;
}

.profile button {
  background-color: inherit;
  border: none;
  font-size: 2vw;
}

</style>