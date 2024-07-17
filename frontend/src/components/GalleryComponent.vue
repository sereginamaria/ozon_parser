<template>
  <div style="display: flex">
    <Galleria :value="this.product.images" v-model:activeIndex="this.gallery.activeIndex" :numVisible="4" :circular="true" containerStyle="width: 800px"
              :showItemNavigators="true">
      <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="display: block; width: 550px" />
      </template>
      <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block; width: 110px" />
      </template>
    </Galleria>
  </div>
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
  },
  mounted() {
    this.product.get_verification_information()
  }
})
</script>

<style scoped>

</style>