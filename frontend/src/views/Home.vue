<template>
  <GalleryComponent/>
  <div style="margin-left: 5%">
    <ToolbarComponent/>
    <div>
      <h3>Пример карточки</h3>
      <p>Нажмите на карточку для увеличения</p>
    </div>
    <div style="display: flex">
      <TitleCardComponent @click="visible = true" :class="'container_025'" :startImageIndex="0"/>
      <CardComponent @click="visible = true" :class="'container_025'" :startImageIndex="0"/>
      <CardComponent @click="visible = true" :class="'container_025'" :startImageIndex="1"/>
    </div>
    <Dialog v-model:visible="visible" modal dismissableMask :draggable="false">
      <div style="display: flex">
        <TitleCardComponent @click="visible = true" :class="'container_05'" :startImageIndex="0"/>
        <CardComponent @click="visible = true" :class="'container_05'" :startImageIndex="0"/>
        <CardComponent @click="visible = true" :class="'container_05'" :startImageIndex="1"/>
      </div>
    </Dialog>

  </div>
</template>

<script>
import {defineComponent} from 'vue'
import GalleryComponent from "@/components/GalleryComponent.vue";
import ToolbarComponent from "@/components/ToolbarComponent.vue";
import CardComponent from "@/components/CardComponent.vue";
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import TitleCardComponent from "@/components/TitleCardComponent.vue";
export default defineComponent ({
  name: "Home",
  components: {TitleCardComponent, CardComponent, ToolbarComponent, GalleryComponent, Button, Dialog},
  data() {
    return {
      visible: false,
    }
  }
})
</script>

<style scoped>

</style>