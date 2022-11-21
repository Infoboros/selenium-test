<template>
  <div class="twit">
    <img :src="avatar" alt="avatar" class="avatar">
    <div class="content">
      <div class="title">

        <h3 id="test_nick_name_twit">
          {{ author.nick_name }}
        </h3>
        <h4 id="test_id_name_twit">
          @{{ author.id_name }}
        </h4>
        <h4>·</h4>
        <h4>
          {{ twit_time }}
        </h4>
      </div>
      <div class="text" id="test_text">
        {{ twitData.text }}
      </div>
      <div class="actions">
        <button :class="{mySelfAction: myRepost}" @click="repost(twitData.id, myId)" id="test_repost">
          <i class="fa fa-retweet" aria-hidden="true"></i>
          <span v-if="repostedUsers.length" id="test_repost_count">{{ repostedUsers.length }}</span>
        </button>
        <button :class="{mySelfAction: myLike}" @click="like(twitData.id, myId)" id="test_like">
          <i class="fa fa-heart-o" aria-hidden="true"></i>
          <span v-if="likedUsers.length" id="test_like_count">{{ likedUsers.length }}</span>
        </button>
        <button><i class="fa fa-share" aria-hidden="true"></i></button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Twit",
  props: ['twitData', 'like', 'repost'],

  computed: {
    author() {
      return this.twitData.author
    },
    twit_time() {
      return new Date(this.twitData.datetime)
          .toLocaleString("ru")
    },
    avatar() {
      const author = this.author
      const avatar = author.avatar

      return avatar ? avatar.url : ''
    },

    events() {
      return this.twitData.event
    },
    myId() {
      return this.$store.state.auth.userId
    },


    repostedUsers() {
      return this.events
          .filter(event => event.type.description === 'Репост')
          .map(event => event.initiator.id)
    },

    likedUsers() {
      return this.events
          .filter(event => event.type.description === 'Лайк')
          .map(event => event.initiator.id)
    },


    myLike() {
      return this.likedUsers
          .includes(this.myId)
    },
    myRepost() {
      return this.repostedUsers
          .includes(this.myId)
    }


  }
}
</script>

<style scoped>
.avatar {
  border-radius: 100%;
  height: 4.5vh;
  width: 4vh;
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
  width: 7%;
}

.twit .content {
  width: 87%;
}

.twit .title {
  display: flex;
  justify-content: start;
}

.twit .content h3 {
  margin: 0 2% 0 0;
}

.twit .content h4 {
  margin: 0 1% 0 0;
  color: rgba(0, 0, 0, 0.6);
}

.twit .content .text {
  font-size: 1vw;
}

.twit .actions {
  display: flex;
  justify-content: space-evenly;

  width: 85%;

  margin-top: 2%;
}

.twit .actions button {
  background-color: #fff;
  border: none;

  font-size: 1.1vw;
}

.twit .actions button:hover {
  cursor: pointer;
  color: #41ABE1;
}

.mySelfAction {
  color: #41ABE1;
}
</style>
