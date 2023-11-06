<script setup>
import Login from "./components/Login.vue";
import work from "./components/work.vue";
</script>

<template>
  <!-- <Login /> -->
  <!-- <work></work> -->
  <div>
    
    <RouterView></RouterView>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
