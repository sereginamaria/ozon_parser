<template>
  <GalleryComponent @updateActiveIndex="updateActiveIndex"/>
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
      activeIndex: 0
    }
  },
  methods: {
    updateActiveIndex(someData) {
      console.log(someData)
    }
  }
})
</script>

<style scoped>

</style>