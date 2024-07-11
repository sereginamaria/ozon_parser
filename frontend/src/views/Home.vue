<template>
  <GalleryComponent/>
  <ToolbarComponent/>
</template>

<script>
import {defineComponent} from 'vue'
import GalleryComponent from "@/components/GalleryComponent.vue";
import ToolbarComponent from "@/components/ToolbarComponent.vue";
export default defineComponent ({
  name: "Home",
  components: {ToolbarComponent, GalleryComponent},
  data() {
    return {
      images: [],
    }
  }
})
</script>

<style scoped>

</style>