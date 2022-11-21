<template>
  <div class="profileInfo">
    <img :src="userData.avatar" alt="avatar" class="avatar">
    <div class="content">
      <h2 id="test_nick_name">
        {{ userData.nick_name }}
      </h2>
      <h3 id="test_id_name">
        @{{ userData.id_name }}
      </h3>
      <p class="registerDate">
        <i class="fa fa-calendar" aria-hidden="true"></i> Регистрация: {{ userData.date_registration }}
      </p>
    </div>
  </div>
</template>

<script>

import {mapGetters} from "vuex";


export default {
  name: "ProfileInfo",

  created() {
    this.$store.dispatch('user/update')
  },

  computed: {
    ...mapGetters('user', ['userData'])
  }
}
</script>

<style scoped>
.profileInfo {
  display: flex;

  justify-content: space-around;

  width: 96%;
  padding: 2%;

  border: solid #e0e0e0 2px;

}

.profileInfo img {
  height: 20vh;
  width: 20vh;
  border-radius: 100%;
}

.profileInfo .content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.profileInfo .content h2 {
  margin: 0;
}

.profileInfo .content h3 {
  margin: 0;
  color: rgba(0, 0, 0, 0.8);
  font-weight: normal;
}
</style>
