<template>
  <Verification :verification="verification_ozon" :goToUrls="goToUrls" :product="product_ozon"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Verification from "@/components/Verification.vue";
import {useVerificationStore, useProductStore} from "@/stores/ozon";
import {mapStores} from "pinia";

export default defineComponent({
  name: "OzonPage",
  data() {
      return {
          goToUrls: ['/wb/verification', '/wb/stylist_panel'],
      }
  },
  components: {Verification},
  computed: {
    ...mapStores(useVerificationStore, useProductStore),
  }
})
</script>


<style scoped>

</style>