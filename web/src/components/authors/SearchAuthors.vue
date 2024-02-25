<template>
  <input
    type="text"
    v-model="userQuery"
    class="input input-bordered w-full"
    placeholder="Search authors"
  />
</template>

<script setup lang="ts">
import { defineModel } from "vue";
const userQuery = defineModel({ required: true, type: String, default: "" });
</script>
