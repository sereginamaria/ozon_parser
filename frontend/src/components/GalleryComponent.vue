<template>
  <Galleria :value="gallery.images" v-model:activeIndex="gallery.activeIndex" :numVisible="4" :circular="true"
            :showItemNavigators="true">
    <template #item="slotProps">
      <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="display: block; height: 100%" />
    </template>
    <template #thumbnail="slotProps">
      <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block; height: 100%" />
    </template>
  </Galleria>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import {useGalleryStore, useProductStore} from '@/stores';

import Galleria from 'primevue/galleria';

export default defineComponent ({
  name: "GalleryComponent",
  components: {
    Galleria
  },
  computed: {
    ...mapStores(useGalleryStore, useProductStore),
  }
})
</script>

<style scoped>

</style>