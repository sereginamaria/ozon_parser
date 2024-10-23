<template>
  <Verification :verification="verification_wb" :labels="labels" :goToUrls="goToUrls" :product="product_wb" :channelName="'@wb_trend_plus'"/>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Verification from "@/components/Verification.vue";
import {useVerificationStore, useProductStore} from "@/stores/wb";
import {mapStores} from "pinia";

export default defineComponent({
  name: "WbPage",
  data() {
      return {
          goToUrls: ['/wb/admin-panel', '/wb/stylist_panel'],
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