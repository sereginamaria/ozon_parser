<template>
  <Verification :verification="verification_wb" :goToUrl="'/wb/admin-panel'" :product="product_wb"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Verification from "@/components/Verification.vue";
import {useVerificationStore, useProductStore} from "@/stores/wb";
import {mapStores} from "pinia";

export default defineComponent({
  name: "WbPage",
  components: {Verification},
  computed: {
    ...mapStores(useVerificationStore, useProductStore),
  }
})
</script>


<style scoped>

</style>