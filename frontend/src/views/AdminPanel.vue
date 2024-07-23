<template>
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
import {defineComponent} from 'vue'

export default defineComponent({
  name: "AdminPanel"
})
</script>

<style scoped>

</style>