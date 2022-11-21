<template>
  <section class="twit">
    <img :src="userData.avatar" alt="avatar" class="avatar">
    <div class="input">
      <form @submit.prevent="makeTwit()">
        <textarea placeholder="Что происходит?" rows="5" v-model="text" id="test_text_twit_field"/>
      </form>
      <div class="actions">
        <button class="sendTwit" @click="makeTwit" id="test_make_twit_button">
          Твитнуть
        </button>
      </div>
    </div>
  </section>
</template>

<script>

import {mapGetters} from "vuex";

export default {
  name: "MakeTwit",
  computed: {
    ...mapGetters('user', ['userData'])
  },
  data() {
    return {
      text: ""
    }
  },
  methods: {
    makeTwit() {
      this.$store.dispatch('feed/makeTwit', this.text)
        .then(() => this.text="")
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

.twit {
  display: flex;
  justify-content: space-evenly;
  align-items: start;

  width: 96%;
  padding: 2%;

  border: solid #e0e0e0 1px;
}

.twit img {
  width: 8%;
}

.twit .input {
  display: flex;
  flex-direction: column;
  width: 90%;
}

.twit .input form {
  display: flex;
  justify-content: center;

  height: 100%;
  width: 100%;

  margin-bottom: 25px;
}

.twit .input form textarea {
  height: 100%;
  width: 94%;

  border: none;

  font-size: 1.5vw;
}

.twit .input .actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;

  border-top: solid #e0e0e0 1px;
  padding-top: 2%;
}

.twit .input .actions .sendTwit {
  width: 30%;
  padding: 1%;
  margin-right: 5%;
}

.sendTwit {
  width: 100%;
  padding: 4%;

  background-color: #41ABE1;

  color: white;
  font-size: 1.4vw;
  font-weight: bold;


  border: none;
  border-radius: 50px;
}

.sendTwit {
  cursor: pointer;
  background-color: #41ABE1;
}

.sendTwit:hover {
  background-color: #288fc0;
}
</style>
