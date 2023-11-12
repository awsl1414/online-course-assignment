<script setup></script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink><span>|</span>
    <RouterLink to="/login">Login</RouterLink><span>|</span>
    <RouterLink to="/404">NotFound</RouterLink>
  </nav>
  <RouterView />
</template>

<style scoped></style>
