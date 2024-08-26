<template>
  <AdminPanel :adminPanel="adminPanel_wb" :goToUrl="'/wb/verification'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import AdminPanel from "@/components/AdminPanel.vue";
import {mapStores} from "pinia";
import {useAdminPanelStore} from "@/stores/wb";

export default defineComponent({
  name: "WbAdminPanel",
  components: {AdminPanel},
    computed: {
    ...mapStores(useAdminPanelStore),
  }
})
</script>


<style scoped>

</style>