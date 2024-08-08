<template>
  <div>
    <div>
      <h3>Информация о товаре</h3>
      <p>Проверефицированных товаров данной категории: {{ product.countOfCategoryProducts }}</p>
      <p>ID: {{ product.id }}</p>
      <p>Категория: {{ product.category }}</p>
      <p>Подкатегория: {{ product.subCategory }}</p>
      <p>Название: {{product.name}}</p>
      <p v-if="product.name.length > 30" style="color: red">В названии более 30 символов! Рекомендовано изменить название!</p>
    </div>
    <div>
      <h3>Работа с изображениями</h3>
      <Button  @click="deleteImage()" label="Удалить" style="margin-right: 1rem"/>
      <Button  @click="visible = true" label="Изменить название"/>
    </div>
    <div>
      <h3>Оставляем товар?</h3>
      <Button label="Да" style="margin-right: 1rem" @click="saveProduct()"/>
      <Button label="Нет" @click="deleteProduct()"/>
    </div>
    <Dialog v-model:visible="visible" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение названия</h3>
        <p>Полное название: {{product.name}}</p>
        <p>Длина названия: {{ product.name.length }}</p>
        <p v-if="product.name.length > 30">Первые 30 символов названия: {{ product.name.slice(0,30) }}</p>
        <InputText type="text" v-model="newName" style="min-width: 300px; margin-right: 1rem"/>
        <Button  label="Сохранить" @click="saveNewName()"/>
      </div>
    </Dialog>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import { useGalleryStore } from '@/stores';
import { useProductStore } from '@/stores';

import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Dialog from "primevue/dialog";

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button, InputText, Dialog},
  data() {
    return {
      visible: false,
      newName: ''
    }
  },
  computed: {
    ...mapStores(useGalleryStore, useProductStore),
  },
  methods: {
    deleteImage(): void {
      this.product.deleteImage(this.gallery.activeIndex)
    },
    saveNewName(): void {
      this.product.saveNewName(this.newName)
      this.visible = false
    },
    saveProduct(): void {
      this.product.saveProduct()
    },
    deleteProduct(): void {
      this.product.deleteProduct()
    }
  },
  mounted() {
    if (this.product.name.length > 30) {
      this.newName = this.product.name.slice(0,30)
    }
    else this.newName = this.product.name
  }
})
</script>

<style scoped>
  .p-dialog-header {
    padding: 0 !important;
  }
</style>