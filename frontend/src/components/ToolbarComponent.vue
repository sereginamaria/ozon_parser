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
      <h3>Оставляем товар?</h3>
      <Button  label="Да" style="margin-right: 5%"/>
      <Button  label="Нет"/>
    </div>
    <div>
      <h3>Изменить имя</h3>
      <p>Полное название: {{this.product.name}}</p>
      <InputText type="text" v-model="this.product.name" />
    </div>
    <div>
      <h3>Работа с данными</h3>
      <div>
        <Button  label="Отложить текущую категорию товаров" style="margin-right: 5%"/>
        <Button  label="Вернуть все отложенные товары"/>
      </div>
      <Button  label="Показать расписание" style="margin-top: 1%"/>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import { useGalleryStore } from '@/stores';
import { useProductStore } from '@/stores';

import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button, InputText},
  computed: {
    ...mapStores(useGalleryStore, useProductStore),
  },
  methods: {
    deleteImage(): void {
      console.log(this.gallery.activeIndex)
      this.product.images.splice(this.gallery.activeIndex, 1)
    }
  }
})
</script>

<style scoped>

</style>