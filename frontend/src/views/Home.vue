<template>
  <GalleryComponent/>
  <div style="margin-left: 5%">
    <ToolbarComponent/>
    <div>
      <h3>Пример карточки</h3>
      <p>Нажмите на карточку для увеличения</p>
    </div>
    <CardComponent @click="visible = true" :class="'container_025'"/>
<!--    <Button label="Посмотреть карточку" @click="visible = true" />-->
    <Dialog v-model:visible="visible" modal dismissableMask :draggable="false">
      <CardComponent :class="'container_05'"/>
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
export default defineComponent ({
  name: "Home",
  components: {CardComponent, ToolbarComponent, GalleryComponent, Button, Dialog},
  data() {
    return {
      visible: false,
    }
  }
})
</script>

<style scoped>

</style>