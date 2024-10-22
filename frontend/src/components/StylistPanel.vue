<template>
  <NavbarComponent :labels="labels" :goToUrls="goToUrls" :channelName="channelName"/>
  <div v-if="stylistPanel.contentReady" class="verification-block-body" :style="'height: calc(100% - ' + height + 'px'">
    <StylistCardComponent :stylistPanel="stylistPanel"/>
  </div>
  <div v-if="!stylistPanel.contentReady">Загрузка... Пожалуйста, подождите!</div>
</template>

<script lang="ts">
  import {defineComponent} from 'vue'
  import NavbarComponent from "@/components/NavbarComponent.vue";
  import StylistCardComponent from "@/components/StylistCardComponent.vue";

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
  components: {StylistCardComponent, NavbarComponent},
  created() {
    this.stylistPanel.get_stylist_panel_information()
  }
})
</script>

<style scoped>

</style>