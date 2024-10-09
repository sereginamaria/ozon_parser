<template>
    <StylistPanel :labels="labels"  :goToUrls="goToUrls"/>
</template>

<script>
import StylistPanel from "@/components/StylistPanel.vue";

export default {
    name: "WbStylistPanel",
    data() {
        return {
            goToUrls: ['/wb/verification', '/wb/admin-panel'],
            labels: ['Верификация', 'Панель Администратора']
        }
    },
    components: {StylistPanel}
}
</script>

<style scoped>

</style>