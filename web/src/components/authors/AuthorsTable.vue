<template>
  <div
    class="overflow-x-auto overflow-y-auto max-h-[90vh] sm:max-h-[80vh] md:max-h-[70vh] lg:max-h-[60vh] xl:max-h-[50vh]"
  >
    <table class="table">
      <thead>
        <tr>
          <th>Full name</th>
          <th>Email</th>
          <th>Age</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody v-for="author in authors" v-bind:key="author.id">
        <tr>
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
import type { AuthorDto } from "@/api/types";

defineProps<{
  authors: AuthorDto[];
}>();
</script>
