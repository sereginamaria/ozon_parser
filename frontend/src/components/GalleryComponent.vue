<template>
  <Galleria :value="this.gallery.images" v-model:activeIndex="this.gallery.activeIndex" :numVisible="4" :circular="true" containerStyle="width: 100%; height: 100%; max-width: 800px"
            :showItemNavigators="true">
    <template #item="slotProps">
      <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="display: block; width: 550px" />
    </template>
    <template #thumbnail="slotProps">
      <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block; width: 110px" />
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