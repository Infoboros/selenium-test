<template>
  <footer class="footer">
    <nav>
      <ul>
        <li><a href="https://twitter.com/tos">Условия предоставления услуг</a></li>
        <li><a href="https://twitter.com/privacy">Политика конфиденциальности</a></li>
        <li><a href="https://support.twitter.com/articles/20170514">Политика в отношении файлов cookie</a>
        </li>
        <li>
          <a href="https://business.twitter.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo">Информация
            о рекламе</a>
        </li>
        <li>© Twitter, Inc., 2021.</li>
      </ul>
    </nav>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>
nav ul {
  list-style: none;
  padding: 0;

  white-space: nowrap;
  font-size: 1vw;

  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 100%;

}

nav ul li {
  color: grey;
  margin: 0.3% 1%;
}

nav ul li a {
  color: inherit;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}

</style>