<template>
  <span class="flex gap-1 items-center">
    <slot>
      <AdAutomation2p />
    </slot>
    {{ value }}
  </span>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { AdAutomation2p } from "@kalimahapps/vue-icons";

export default defineComponent({
  components: {
    AdAutomation2p,
  },
  props: {
    value: {
      type: String,
      required: true,
    },
    icon: {
      type: Object,
      default: () => AdAutomation2p,
    },
  },
});
</script>
