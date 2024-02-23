<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">Digital Library</a>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal px-1">
        <li>
          <a><RouterLink to="/">Home</RouterLink></a>
        </li>
        <li>
          <RouterLink to="/authors">Authors</RouterLink>
        </li>
      </ul>
    </div>
  </div>
  <RouterView />
</template>

<style scoped></style>
