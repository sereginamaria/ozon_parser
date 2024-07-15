<template>
  <div>
    <div>
      <h3>Информация о товаре</h3>
      <p>ID: {{ this.product.id }}</p>
      <p>Категория: {{ this.product.category }}</p>
      <p>Подкатегория: {{ this.product.subCategory }}</p>
      <p>Название: {{ this.product.name }}</p>
    </div>
    <div>
      <h3>Работа с изображениями</h3>
      <Button  @click="deleteImage()" label="Удалить"/>
    </div>
    <div>
      <p>Оставляем товар?</p>
      <Button  label="Да"/>
      <Button  label="Нет"/>
    </div>
    <div>
      <p>Изменить имя</p>
      <Button  label="Да"/>
      <Button  label="Нет"/>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import { useGalleryStore } from '@/stores';
import { useProductStore } from '@/stores';

import Button from 'primevue/button';

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button},
  computed: {
    ...mapStores(useGalleryStore, useProductStore),
  },
  methods: {
    deleteImage(): void {
      console.log(this.gallery.activeIndex)
    }
  }
})
</script>

<style scoped>

</style>