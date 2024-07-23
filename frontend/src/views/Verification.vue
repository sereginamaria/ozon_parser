<template>
  <div v-if="this.gallery.contentReady" class="verification">
    <NavbarComponent :label="'Панель Администратора'" :goToUrl="'/admin-panel'"/>

    <div class="gallery" :style="'height: calc(100% - ' + this.height + 'px'">
      <GalleryComponent/>
      <div style="padding: 2%; max-width: 800px">
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
import NavbarComponent from "@/components/NavbarComponent.vue";

export default defineComponent ({
  name: "Verification",
  components: {
    NavbarComponent,
    TitleCardComponent, CardComponent, ToolbarComponent, GalleryComponent, Button, Dialog, Toolbar},
  data() {
    return {
      visible: false,
      height: 0
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
  mounted() {
    if (document.getElementById('toolbar') != null) {
      this.height = document.getElementById('toolbar').offsetHeight
    }
  },
  updated() {
    this.$nextTick(function () {
      this.height = document.getElementById('toolbar').offsetHeight
    })
  },
  created() {
    window.addEventListener('beforeunload', () => {
      this.$router.push('/')
    });

    this.product.get_verification_information()
  }

})
</script>

<style scoped>
  .verification {
    width: 100%;
    height: 100%;
  }

  .gallery {
    width: 100%;
    display: flex;
    justify-content: center;
  }
</style>