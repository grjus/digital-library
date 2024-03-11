<script lang="ts">
import axios from "axios";
import { defineComponent, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import type { AuthorDtoWithDetails } from "@/api/types";
import {
  ThCup,
  ByBook,
  AkFacebookFill,
  AkInstagramFill,
  AkTwitterFill,
  IcWww,
} from "@kalimahapps/vue-icons";

import IconValue from "@/components/authors/IconValue.vue";
import AuthorSection from "@/components/authors/AuthorSection.vue";

export default defineComponent({
  components: {
    ThCup,
    ByBook,
    IconValue,
    AkFacebookFill,
    AkInstagramFill,
    AkTwitterFill,
    IcWww,
    AuthorSection,
  },

  setup() {
    const route = useRoute();
    const author = ref({} as AuthorDtoWithDetails);

    async function fetchAuthorData() {
      const response = await axios.get<AuthorDtoWithDetails>(
        `/api/authors/${route.params.id}`
      );
      try {
        const data = response.data;
        author.value = data;
      } catch (error) {
        console.error(error);
      }
    }

    onMounted(() => {
      fetchAuthorData();
    });

    const getPlatformIcon = (platform: string) => {
      console.log(platform);
      switch (platform) {
        case "facebook":
          return AkFacebookFill;
        case "twitter":
          return "AkTwitterFill";
        case "instagram":
          return "AkInstagramFill";
        default:
          return AkFacebookFill;
      }
    };

    return {
      author,
      getPlatformIcon,
    };
  },
});
</script>

<template>
  <div v-if="author" class="card card-side bg-base-100 shadow-xl">
    <div class="card-body flex flex-col gap-4">
      <AuthorSection :label="'Name'">
        {{ author.fullname }}
      </AuthorSection>
      <AuthorSection :label="'Biography'">
        <p class="article w-[70%]">{{ author.author_details?.bio }}</p>
      </AuthorSection>
      <AuthorSection
        v-if="
          author.author_details?.awards &&
          author.author_details?.awards?.length > 0
        "
        :label="'Awards'"
      >
        <ul>
          <li
            v-for="(award, index) in author.author_details?.awards"
            class="py-1"
            :key="index"
          >
            <IconValue :value="award">
              <ThCup />
            </IconValue>
          </li>
        </ul>
      </AuthorSection>
      <AuthorSection
        v-if="
          author.author_details?.awards &&
          author.author_details?.awards?.length > 0
        "
        :label="'Awards'"
      >
        <ul>
          <li
            v-for="(award, index) in author.author_details?.awards"
            class="py-1"
            :key="index"
          >
            <IconValue :value="award">
              <ThCup />
            </IconValue>
          </li>
        </ul>
      </AuthorSection>

      <AuthorSection
        v-if="
          author.author_details?.published_books &&
          author.author_details?.published_books.length > 0
        "
        :label="'Published Books'"
      >
        <ul>
          <li
            v-for="(book, index) in author.author_details?.published_books"
            :key="index"
            class="py-1"
          >
            <IconValue :value="book">
              <ByBook />
            </IconValue>
          </li>
        </ul>
      </AuthorSection>

      <AuthorSection :label="'Nationality'">
        <p>{{ author.author_details?.nationality }}</p>
      </AuthorSection>
    </div>
    <div class="flex flex-col w-full items-center">
      <div class="rounded-full bg-slate-700">
        <img
          :src="author.author_details?.photo_url"
          alt="Author Image"
          class="rounded-t-lg"
        />
      </div>
      <div>
        <div class="flex gap-4 mt-8 flex-wrap">
          <a
            class="btn btn-info btn-sm w-32"
            :href="author.author_details?.website"
            target="_blank"
            ><IcWww />Website</a
          >
          <a
            v-for="(link, platform) in author.author_details
              ?.social_media_links"
            :key="platform"
            :href="link"
            target="_blank"
            class="btn btn-info btn-sm w-32"
          >
            <component :is="getPlatformIcon(platform)" />
            {{ platform }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
