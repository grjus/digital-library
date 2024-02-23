<template>
  <div class="overflow-x-auto overflow-y-auto h-[400px]">
    <table class="table">
      <thead>
        <tr>
          <th></th>
          <th>Full name</th>
          <th>Email</th>
          <th>Age</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody v-for="author in authors" v-bind:key="author.id">
        <tr>
          <th>{{ author.id }}</th>
          <td>{{ author.fullname }}</td>
          <td>{{ author.email }}</td>
          <td>{{ author.age }}</td>
          <td>
            <button class="btn btn-active btn-info btn-sm">View details</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import axios from "axios";
import { ref } from "vue";
import { AuthorDto } from "@/api/types.d.ts";
const authors = ref<AuthorDto[]>([]);

async function fetchAuthors() {
  const response = await axios.get("api/author");
  const data = await response.data;
  authors.value = data;
}

onMounted(() => {
  fetchAuthors();
});
</script>
