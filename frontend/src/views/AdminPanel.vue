<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="'/'"/>
  <div>
      <h3>Работа с данными</h3>
      <div>
        <Button  label="Отложить текущую категорию товаров" style="margin-right: 5%"/>
        <Button  label="Вернуть все отложенные товары"/>
      </div>
      <Button  label="Показать расписание" style="margin-top: 1%"/>
  </div>
</template>

<script lang="ts">
import Button from 'primevue/button';
import {defineComponent} from 'vue'
import NavbarComponent from "@/components/NavbarComponent.vue";

export default defineComponent({
  name: "AdminPanel",
  components: {NavbarComponent, Button},
})
</script>

<style scoped>

</style>