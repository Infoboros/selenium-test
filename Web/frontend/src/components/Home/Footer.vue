<template>
  <footer>
    <nav class="navigation">
      <ul>
        <FooterLi v-for="(link, index) in links" :key="index" :href="link.href" :text="link.text"/>
      </ul>
    </nav>
  </footer>
</template>

<script>

import FooterLi from "./FooterLi";

export default {
  name: "Footer",
  components: {
    FooterLi
  },
  data() {
    return {
      links: [
        {href: 'https://about.twitter.com/', text: 'О нас'},
        {href: 'https://help.twitter.com/', text: 'Справочный центр'},
        {href: 'https://twitter.com/tos', text: 'Условия предоставления услуг'},
        {href: 'https://twitter.com/privacy', text: 'Политика конфиденциальности'},
        {href: 'https://support.twitter.com/articles/20170514', text: 'Политика в отношении файлов cookie'},
        {href: 'https://business.twitter.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo', text: 'Информация о рекламе'},
        {href: 'https://blog.twitter.com/', text: 'Блог'},
        {href: 'https://status.twitterstat.us/', text: 'Статус'},
        {href: 'https://careers.twitter.com/', text: 'Работа'},
        {href: 'https://about.twitter.com/press/brand-assets', text: 'Ресурсы бренда'},
        {href: 'https://ads.twitter.com/?ref=gl-tw-tw-twitter-advertise', text: 'Реклама'},
        {href: 'https://marketing.twitter.com/', text: 'Маркетинг'},
        {href: 'https://business.twitter.com/?ref=web-twc-ao-gbl-twitterforbusiness&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=twitterforbusiness', text: 'Твиттер для бизнеса'},
        {href: 'https://developer.twitter.com/', text: 'Разработчикам'},
        {href: 'https://twitter.com/i/directory/profiles', text: 'Каталог'},
        {href: 'https://twitter.com/settings', text: 'Настройки'},
        {href: 'https://twitter.com/', text: '© Twitter, Inc., 2021.'}
      ]
    }
  }
}
</script>

<style scoped>
footer {
  height: 10%;
}

ul {
  list-style: none;
  padding: 0;

  white-space: nowrap;
  font-size: 1vw;

  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  max-width: 100%;
}
</style>