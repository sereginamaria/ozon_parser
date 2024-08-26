<template>
  <AdminPanel :adminPanel="adminPanel_ozon" :goToUrl="'/ozon/verification'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import AdminPanel from "@/components/AdminPanel.vue";
import {mapStores} from "pinia";
import {useAdminPanelStore} from "@/stores/ozon";

export default defineComponent({
  name: "OzonAdminPanel",
  components: {AdminPanel},
    computed: {
    ...mapStores(useAdminPanelStore),
  }
})
</script>


<style scoped>

</style>