<script lang="ts">
import axios from "axios";
import { defineComponent, onMounted, ref } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  setup() {
    const route = useRoute();
    const state = ref({});

    async function fetchAuthorData() {
      const response = await axios.get<any>(`/api/author/${route.params.id}`);
      try {
        const data = response.data;
        console.log("asdasd");
        console.log(data);
        state.value = data;
      } catch (error) {
        console.error(error);
      }
    }

    onMounted(() => {
      fetchAuthorData();
    });

    console.log(state.value);
  },
});
</script>

<template>
  <p>This is an author page</p>
</template>
