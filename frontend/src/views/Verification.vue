<template>
  <div v-if="this.gallery.contentReady">
    <Toolbar style="padding: 1rem 1rem 1rem 1.5rem">
      <template #start>
        <div class="flex items-center gap-2">
          <Button label="Панель администратора" text plain @click="goToAdminPanel()"/>
        </div>
      </template>
    </Toolbar>

    <div style="display: flex">
      <GalleryComponent/>
      <div style="margin-left: 5%">
        <ToolbarComponent/>
        <div>
          <h3>Пример карточки</h3>
          <p>Нажмите на карточку для увеличения</p>
        </div>
        <div style="display: flex">
          <TitleCardComponent @click="visible = true" :class="'container_025'" :startImageIndex="0"/>
          <CardComponent @click="visible = true" :class="'container_025'" :startImageIndex="1"/>
          <CardComponent @click="visible = true" :class="'container_025'" :startImageIndex="0"/>
        </div>
        <Dialog v-model:visible="visible" modal dismissableMask :draggable="false">
          <div style="display: flex">
            <TitleCardComponent @click="visible = true" :class="'container_05'" :startImageIndex="0"/>
            <CardComponent @click="visible = true" :class="'container_05'" :startImageIndex="1"/>
            <CardComponent @click="visible = true" :class="'container_05'" :startImageIndex="0"/>
          </div>
        </Dialog>
      </div>
    </div>
  </div>
  <div v-else>Загрузка... Пожалуйста, подождите!</div>
</template>

<script>
import {defineComponent} from 'vue'
import GalleryComponent from "@/components/GalleryComponent.vue";
import ToolbarComponent from "@/components/ToolbarComponent.vue";
import CardComponent from "@/components/CardComponent.vue";
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import Toolbar from 'primevue/toolbar';
import TitleCardComponent from "@/components/TitleCardComponent.vue";
import {mapStores} from "pinia";
import {useGalleryStore, useProductStore} from "@/stores";
export default defineComponent ({
  name: "Verification",
  components: {TitleCardComponent, CardComponent, ToolbarComponent, GalleryComponent, Button, Dialog, Toolbar},
  data() {
    return {
      visible: false,
    }
  },
  computed: {
    ...mapStores(useGalleryStore, useProductStore),
  },
  methods: {
      goToAdminPanel(){
          this.$router.push('/admin-panel')
      }
  },
  created() {
    window.addEventListener('beforeunload', () => {
      this.$router.push('/verification')
    });

    this.product.get_verification_information()
  }

})
</script>

<style scoped>

</style>