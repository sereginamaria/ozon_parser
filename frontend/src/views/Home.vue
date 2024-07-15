<template>
  <GalleryComponent/>
  <div>
    <ToolbarComponent/>
    <CardComponent/>
  </div>
</template>

<script>
import {defineComponent} from 'vue'
import GalleryComponent from "@/components/GalleryComponent.vue";
import ToolbarComponent from "@/components/ToolbarComponent.vue";
import CardComponent from "@/components/CardComponent.vue";
export default defineComponent ({
  name: "Home",
  components: {CardComponent, ToolbarComponent, GalleryComponent},
  data() {
    return {
      images: [],
    }
  }
})
</script>

<style scoped>

</style>