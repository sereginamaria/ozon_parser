<template>
  <div>
    <div>
      <div>
        <h3>Работа с изображениями</h3>
        <Button  @click="deleteImage()" label="Удалить" class="toolbar-block__button"/>
        <Button  @click="visibleChangeName = true" label="Изменить название" class="toolbar-block__button"/>
        <Button  @click="visibleChangeSubCategory = true" label="Изменить подкатегорию"/>
      </div>
      <div>
        <h3>Оставляем товар?</h3>
        <Button label="Да" style="margin-right: 1rem" @click="saveProduct()"/>
        <Button label="Нет" @click="deleteProduct()"/>
      </div>
      <h3>Информация о товаре</h3>
      <p>Проверефицированных товаров данной категории: {{ product.countOfCategoryProducts }}</p>
      <p>ID: {{ product.id }}</p>
      <p>Категория: {{ product.category }}</p>
      <p>Подкатегория: {{ product.subCategory }}</p>
      <p>Название: {{product.name}}</p>
      <p v-if="product.name.length > 30" style="color: red">В названии более 30 символов! Рекомендовано изменить название!</p>
    </div>

    <Dialog v-model:visible="visibleChangeName" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение названия</h3>
        <p>Полное название: {{product.name}}</p>
        <p>Длина названия: {{ product.name.length }}</p>
        <p v-if="product.name.length > 30">Первые 30 символов названия: {{ product.name.slice(0,30) }}</p>
        <InputText type="text" v-model="newName" style="min-width: 300px; margin-right: 1rem"/>
        <Button  label="Сохранить" @click="saveNewName()"/>
      </div>
    </Dialog>

    <Dialog v-model:visible="visibleChangeSubCategory" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение подкатегории</h3>
        <p>Текущая подкатегория: {{product.subCategory}}</p>
        <InputText type="text" v-model="newSubCategory" style="min-width: 300px; margin-right: 1rem"/>
        <Button  label="Сохранить" @click="saveNewSubCategory()"/>
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
      visibleChangeName: false,
      visibleChangeSubCategory: false,
      newName: '',
      newSubCategory: ''
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
      this.visibleChangeName = false
    },
    saveNewSubCategory(): void {
      this.product.saveNewSubCategory(this.newSubCategory)
      this.visibleChangeSubCategory = false
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

    this.newSubCategory = this.product.subCategory
  }
})
</script>

<style scoped>
  .p-dialog-header {
    padding: 0 !important;
  }

  .toolbar-block__button {
    margin-right: 1rem;
    margin-bottom: 1rem
  }

  @media screen and (max-width: 480px) {
    .toolbar-block__button {
      margin-bottom: 0.5rem
    }
  }
</style>