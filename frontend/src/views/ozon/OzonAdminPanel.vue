<template>
  <AdminPanel :adminPanel="adminPanel_ozon" :goToUrls="goToUrls"/>
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
          goToUrls: ['/wb/verification', '/wb/stylist_panel'],
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