<template>
  <NavbarComponent :labels="labels" :goToUrls="goToUrls" :channelName="channelName"/>
  <div v-if="stylistPanel.contentReady" class="verification-block-body" :style="'height: calc(100% - ' + height + 'px'">
    <StylistCardComponent :stylistPanel="stylistPanel" :channelName="channelName"/>
    <div>
        <h3>Оставляем образ?</h3>
        <Button label="Да" style="margin-right: 1rem; min-width: 50px;" @click="saveStyledCard()"/>
        <Button label="Нет" @click="deleteStyledCard()" style="min-width: 50px;"/>
    </div>
  </div>
  <div v-if="!stylistPanel.contentReady">Загрузка... Пожалуйста, подождите!</div>
</template>

<script lang="ts">
  import {defineComponent} from 'vue'
  import NavbarComponent from "@/components/NavbarComponent.vue";
  import StylistCardComponent from "@/components/StylistCardComponent.vue";
  import Button from 'primevue/button';

  export default defineComponent({
  name: "StylistPanel",
  props: {
    goToUrls: {
        type: Array,
        default: []
    },
    labels: {
        type: Array,
        default: []
    },
    stylistPanel: {
      type: Object,
      default: {}
    },
    channelName:{
        type: String,
        default: ''
    }
  },
  components: {StylistCardComponent, NavbarComponent, Button},
  methods: {
      saveStyledCard(){
          this.stylistPanel.saveStyledCard()
      },
      deleteStyledCard() {
          this.stylistPanel.deleteStyledCard()
      }
  },
  created() {
      console.log('gi')
      this.stylistPanel.get_stylist_panel_information()
  }
})
</script>

<style scoped>

</style>