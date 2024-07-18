<template>
  <div>
    <div>
      <h3>Информация о товаре</h3>
      <p>ID: {{ this.product.id }}</p>
      <p>Категория: {{ this.product.category }}</p>
      <p>Подкатегория: {{ this.product.subCategory }}</p>
      <p>Название: {{this.product.name}}</p>
      <p v-if="this.product.name.length > 30" style="color: red">В названии более 30 символов! Рекомендовано изменить название!</p>
    </div>
    <div>
      <h3>Работа с изображениями</h3>
      <Button  @click="deleteImage()" label="Удалить" style="margin-right: 5%"/>
      <Button  @click="this.visible = true" label="Изменить название"/>
    </div>
    <div>
      <h3>Оставляем товар?</h3>
      <Button  label="Да" style="margin-right: 5%"/>
      <Button  label="Нет"/>
    </div>
    <Dialog v-model:visible="visible" modal dismissableMask :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение названия</h3>
        <p>Полное название: {{this.product.name}}</p>
        <p>Длина названия: {{ this.product.name.length }}</p>
        <p v-if="this.product.name.length > 30">Первые 30 символов названия: {{ this.product.name.slice(0,30) }}</p>
        <InputText type="text" v-model="this.newName" />
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
    }
  }
})
</script>

<style scoped>

</style>