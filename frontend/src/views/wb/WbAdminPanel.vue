<template>
  <AdminPanel :adminPanel="adminPanel_wb" :labels="labels" :goToUrls="goToUrls" :channelName="'@wb_trend_plus'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import AdminPanel from "@/components/AdminPanel.vue";
import {mapStores} from "pinia";
import {useAdminPanelStore} from "@/stores/wb";

export default defineComponent({
  name: "WbAdminPanel",
  data() {
      return {
          goToUrls: ['/wb/verification', '/wb/stylist_panel'],
          labels: ['pi pi-check-square', 'pi pi-palette']
      }
  },
  components: {AdminPanel},
    computed: {
    ...mapStores(useAdminPanelStore),
  }
})
</script>


<style scoped>

</style>