<template>
  <div>
    <h1>Добро пожаловать!</h1>
    <Button @click="goToVerification">Верификация</Button>
  </div>
</template>

<script>
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import {useProductStore} from '@/stores';
import Button from 'primevue/button'

export default defineComponent ({
  name: "Home",
  components: {Button},
  computed: {
    ...mapStores(useProductStore),
  },
  methods: {
    goToVerification() {
      this.$router.push('/verification')
    },
  },

})
</script>

<style scoped>

</style>