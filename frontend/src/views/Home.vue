<template>
  <div class="home-block">
    <Button label="OZON" @click="goToOzon()" style="margin-right: 1rem;"/>
    <Button label="WB" @click="goToWb()"/>
  </div>

</template>

<script lang="ts">
import Button from 'primevue/button';
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Home",
  components: {
    Button
  },
  methods: {
    goToOzon(){
      this.$router.push('/ozon/verification')
    },
    goToWb(){
      this.$router.push('/wb/verification')
    }
  }
})
</script>

<style scoped>
  .home-block {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>