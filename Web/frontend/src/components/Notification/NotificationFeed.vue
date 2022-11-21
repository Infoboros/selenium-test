<template>
  <div class="notificationFeed" id="test_notification_feed">
    <Title/>
    <NotificationItem v-for="(item, index) in eventsList" :key="index"
                      :i-class="item.iClass"
                      :title="item.title"
                      :text="item.text"
                      id="test_notification"
    />
  </div>
</template>

<script>

import Title from "./Title";
import NotificationItem from "./NotificationItem";

export default {
  name: "NotificationFeed",
  created() {
    this.$store.dispatch('events/update')
  },
  computed: {
    eventsList(){
      return this.$store.getters["events/events"]
      .map(event => {
        const {nick_name} = event.initiator

        if (event.type.description === 'Лайк')
          return {
            iClass: 'fa fa-heart',
            title: 'Ваш твит нравится людям.',
            text: `Пользователь ${nick_name} поставил вашему твиту лайк.`
          }
        else
          return {
            iClass: 'fa fa-retweet',
            title: 'Люди делятся вашими твитами.',
            text: `Пользователь ${nick_name} сделал репост вашего твита.`
          }
      })
    }
  },
  components: {
    Title,
    NotificationItem
  }
}
</script>

<style scoped>
.notificationFeed {
  width: 55%;
  height: 100%;

  overflow: scroll;

  border: solid #e0e0e0 1px;
  border-top: none;
  border-bottom: none;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>
