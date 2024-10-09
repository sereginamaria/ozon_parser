<template>
    <NavbarComponent :labels="labels" :goToUrls="goToUrls"/>
  <StylistCardComponent/>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";
import StylistCardComponent from "@/components/StylistCardComponent.vue";

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
    components: {StylistCardComponent, NavbarComponent}
}
</script>

<style scoped>

</style>