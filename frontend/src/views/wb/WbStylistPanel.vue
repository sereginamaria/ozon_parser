<template>
    <StylistPanel :labels="labels" :goToUrls="goToUrls" :stylistPanel="stylistPanel_wb" :channelName="'@wb_trend_plus'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import StylistPanel from "@/components/StylistPanel.vue";
import {mapStores} from "pinia";
import {useProductStore, useStylistPanelStore} from "@/stores/wb";

export default defineComponent({
    name: "WbStylistPanel",
    data() {
        return {
            goToUrls: ['/wb/verification', '/wb/admin-panel'],
            labels: ['Верификация', 'Панель Администратора']
        }
    },
    components: {StylistPanel},
  computed: {
    ...mapStores(useStylistPanelStore),
  }
})
</script>

<style scoped>

</style>