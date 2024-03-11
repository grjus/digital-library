<template>
  <SearchAuthors v-model="userQuery" />
  <AuthorsTable :authors="authorsPayload.authors" />
  <AuthorsTablePagination
    :pageNumber="pageNumber"
    @nextPage="nextPage"
    @previousPage="previousPage"
    v-model="pageSize"
    :nextPage="authorsPayload.next_page"
  />
</template>

<script setup lang="ts">
import type { AuthorDto } from "@/api/types";
import AuthorsTable from "@/components/authors/AuthorsTable.vue";
import AuthorsTablePagination from "@/components/authors/AuthorsTablePagination.vue";
import SearchAuthors from "@/components/authors/SearchAuthors.vue";
import { useDebounceFn } from "@vueuse/core";
import axios from "axios";
import { onMounted, ref, watch } from "vue";

type AuthorDtoPageable = {
  authors: AuthorDto[];
  total_authors: number;
  page_number: number;
  page_size: number;
  next_page: boolean;
};

const authorsPayload = ref<AuthorDtoPageable>({
  authors: [],
  total_authors: 0,
  page_number: 0,
  page_size: 10,
  next_page: false,
});

const userQuery = ref("");
const pageNumber = ref(1);
const pageSize = ref<string>("5");

async function fetchAuthors() {
  const response = await axios.get<AuthorDtoPageable>("/api/authors/", {
    params: {
      query: userQuery.value,
      page_number: pageNumber.value,
      page_size: pageSize.value,
    },
  });
  try {
    const data = response.data;
    authorsPayload.value = data;
  } catch (error) {
    console.error(error);
  }
}

const nextPage = () => {
  pageNumber.value++;
  fetchAuthors();
};

const previousPage = () => {
  if (pageNumber.value === 1) return;
  pageNumber.value--;
  fetchAuthors();
};

onMounted(() => {
  fetchAuthors();
});

watch(
  userQuery,
  useDebounceFn(() => {
    pageNumber.value = 1;
    fetchAuthors();
  }, 200),
  { immediate: false },
);

watch(pageSize, () => {
  pageNumber.value = 1;
  fetchAuthors();
});
</script>
