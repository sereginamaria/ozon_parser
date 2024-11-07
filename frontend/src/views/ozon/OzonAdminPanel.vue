<template>
  <AdminPanel :adminPanel="adminPanel_ozon" :labels="labels" :goToUrls="goToUrls" :channelName="'@ozon_trend_plus'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import AdminPanel from "@/components/AdminPanel.vue";
import {mapStores} from "pinia";
import {useAdminPanelStore} from "@/stores/ozon";

export default defineComponent({
  name: "OzonAdminPanel",
  data() {
    return {
      goToUrls: ['/ozon/verification', '/ozon/stylist_panel'],
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