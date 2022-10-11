<template>
  <li>
    <a :href="href">{{text}}</a>
  </li>
</template>

<script>
export default {
  name: "FooterLi",
  props: [
      'href',
      'text'
  ]
}
</script>

<style scoped>
li {
  color: grey;
  margin: 0.3% 1%;
}

li a {
  color: inherit;
  text-decoration: none;
}

li a:hover {
  text-decoration: underline;
}
</style>