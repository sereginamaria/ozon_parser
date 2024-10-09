<template>
    <NavbarComponent :labels="labels" :goToUrls="goToUrls"/>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";

export default {
    name: "StylistPanel",
    props: {
        goToUrls: {
            type: Array,
            default: []
        },
        labels: {
            type: Array,
            default: []
        }
    },
    components: {NavbarComponent}
}
</script>

<style scoped>

</style>