<template>
  <Galleria :value="verification.images" v-model:activeIndex="verification.activeIndex" :numVisible="4" :circular="true"
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
import Galleria from 'primevue/galleria';

export default defineComponent ({
  name: "GalleryComponent",
  props: {
    verification: {
      type: Object,
      default: {}
    }
  },
  components: {
    Galleria
  }
})
</script>

<style scoped>

</style>