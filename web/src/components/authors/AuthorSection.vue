<template>
  <div class="flex flex-col gap-2">
    <h2 class="text-lg font-semibold">{{ label }}</h2>
    <div class="flex gap-2">
      <slot> </slot>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  label: String,
});
</script>
```
