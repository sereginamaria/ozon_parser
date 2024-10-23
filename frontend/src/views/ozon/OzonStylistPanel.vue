<template>
    <StylistPanel :labels="labels" :goToUrls="goToUrls" :stylistPanel="stylistPanel_ozon" :channelName="'@ozon_trend_plus'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import StylistPanel from "@/components/StylistPanel.vue";
import {mapStores} from "pinia";
import {useStylistPanelStore} from "@/stores/ozon";

export default defineComponent({
    name: "OzonStylistPanel",
    data() {
        return {
            goToUrls: ['/ozon/verification', '/ozon/admin-panel'],
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