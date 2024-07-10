<template>
  <GalleryComponent :activeIndex="activeIndex"/>
  <ToolbarComponent :activeIndex="activeIndex"/>
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
      activeIndex1: 0
    }
  },
  computed: {
    activeIndex() {
      console.log(this.activeIndex1)
      return this.activeIndex1
    }
  }
})
</script>

<style scoped>

</style>