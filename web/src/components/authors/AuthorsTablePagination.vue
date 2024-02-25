<template>
  <div class="flex justify-between gap-2 items-center">
    <select class="select select-bordered max-w-xs" v-model="pageSize">
      <option value="5">5 records per page</option>
      <option value="10">10 records per page</option>
      <option value="20">20 records per page</option>
    </select>
    <div class="join">
      <button
        class="join-item btn"
        :class="pageNumber == 1 ? 'btn-disabled' : ''"
        @click="$emit('previousPage')"
      >
        «
      </button>
      <button class="join-item btn">Page {{ pageNumber }}</button>
      <button
        class="join-item btn"
        :class="!nextPage ? 'btn-disabled' : ''"
        @click="$emit('nextPage')"
      >
        »
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineEmits(["nextPage", "previousPage"]);
defineProps({
  pageNumber: Number,
  nextPage: Boolean,
});
const pageSize = defineModel({ required: true, type: String });
</script>
