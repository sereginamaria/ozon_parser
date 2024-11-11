<template>
  <div class="verification-block">
    <NavbarComponent :labels="labels" :goToUrls="goToUrls" :channelName="channelName"/>

    <div v-if="verification.contentReady" class="verification-block-body" :style="'height: calc(100% - ' + height + 'px'">
      <GalleryComponent :verification="verification"/>
      <div class="toolbar">
        <ToolbarComponent :product="product" :verification="verification"/>
        <div>
          <h3>Пример карточки</h3>
          <p>Нажмите на карточку для увеличения</p>
        </div>
        <div style="display: flex; flex-wrap: wrap">
          <TitleCardComponent @click="visible = true" :cardClass="'container_025'" :startImageIndex="0" :product="product"/>
          <CardComponent @click="visible = true" :cardClass="'container_025'" :startImageIndex="0" :product="product"/>
          <CardComponent @click="visible = true" :cardClass="'container_025'" :startImageIndex="2" :product="product"/>
        </div>
        <Dialog v-model:visible="visible" modal dismissableMask :draggable="false">
          <div style="display: flex; flex-wrap: wrap">
            <TitleCardComponent @click="visible = true" :cardClass="'container_05'" :startImageIndex="0" :product="product"/>
            <CardComponent @click="visible = true" :cardClass="'container_05'" :startImageIndex="0" :product="product"/>
            <CardComponent @click="visible = true" :cardClass="'container_05'" :startImageIndex="2" :product="product"/>
          </div>
        </Dialog>
      </div>
    </div>
    <div v-if="verification.contentEmpty">Все товары проверифицированы!</div>
    <div v-if="!verification.contentReady && !verification.contentEmpty">Загрузка... Пожалуйста, подождите!</div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import GalleryComponent from "@/components/GalleryComponent.vue";
import ToolbarComponent from "@/components/ToolbarComponent.vue";
import CardComponent from "@/components/CardComponent.vue";
import Dialog from 'primevue/dialog'
import Toolbar from 'primevue/toolbar';
import TitleCardComponent from "@/components/TitleCardComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";

export default defineComponent ({
  name: "Verification",
  components: {
    NavbarComponent,
    TitleCardComponent, CardComponent, ToolbarComponent, GalleryComponent, Dialog, Toolbar
  },
  props: {
    verification: {
      type: Object,
      default: {}
    },
    product: {
      type: Object,
      default: {}
    },
    goToUrls: {
      type: Array,
      default: []
    },
    labels: {
        type: Array,
        default: []
    },
      channelName:{
          type: String,
          default: ''
      }
  },
  data() {
    return {
      visible: false,
      height: 0
    }
  },
  methods: {
    leftScroll(e){
        if (e.code === 'ArrowLeft' || e.code === 'KeyA'){
            if (this.verification.activeIndex != 0){
                this.verification.activeIndex -= 1
            }
            else{
                this.verification.activeIndex = this.product.images.length - 1
            }
        }
        if (e.code === 'ArrowRight' || e.code === 'KeyD'){
            if (this.verification.activeIndex < (this.product.images.length - 1)){
                this.verification.activeIndex += 1
            }
            else {
                this.verification.activeIndex = 0
            }
        }
    }
  },
  mounted() {
      const toolBarElement = document.getElementById('toolbar')

      if (toolBarElement !== null) {
        this.height = document.getElementById('toolbar')!.offsetHeight
      }

      document.addEventListener( "keydown", this.leftScroll );
  },
  updated() {
    this.$nextTick(function () {
      const toolBarElement = document.getElementById('toolbar')

      if (toolBarElement !== null) {
        this.height = document.getElementById('toolbar')!.offsetHeight
      }
    })
  },
  created() {
    this.verification.get_verification_information()
  }

})
</script>

<style scoped>
  .verification-block {
    width: 100%;
    height: 100%;
  }

  .verification-block-body {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .toolbar {
    padding: 0 1rem 1rem 2rem;
    max-width: 50%
  }

  @media screen and (max-width: 480px) {
    .toolbar {
      max-width: 100%;
      padding: 0 0.5rem 0.5rem 0.5rem;
    }
    .verification-block-body {
      flex-wrap: wrap;
    }
  }
</style>