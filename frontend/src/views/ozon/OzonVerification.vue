<template>
  <Verification :verification="verification_ozon" :goToUrl="'/ozon/admin-panel'" :product="product_ozon"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Verification from "@/components/Verification.vue";
import {useVerificationStore, useProductStore} from "@/stores/ozon";
import {mapStores} from "pinia";

export default defineComponent({
  name: "OzonPage",
  components: {Verification},
  computed: {
    ...mapStores(useVerificationStore, useProductStore),
  }
})
</script>


<style scoped>

</style>