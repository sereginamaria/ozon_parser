<template>
  <Verification :verification="verification_ozon" :labels="labels" :goToUrls="goToUrls" :product="product_ozon"/>
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
      goToUrls: ['/admin-panel', '/stylist_panel'],
      labels: ['Панель Администратора', 'Стилист']
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