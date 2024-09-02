<template>
  <div>
    <div>
      <div>
        <h3>Работа с изображениями</h3>
        <Button  @click="deleteImage()" label="Удалить" class="toolbar-block__button"/>
        <Button  @click="visibleChangeName = true" label="Изменить название" class="toolbar-block__button"/>
      </div>
      <div>
        <h3>Оставляем товар?</h3>
        <Button label="Да" style="margin-right: 1rem; min-width: 50px;" @click="saveProduct()"/>
        <Button label="Нет" @click="deleteProduct()" style="min-width: 50px;"/>
      </div>
      <h3>Информация о товаре</h3>
      <p>Категория: {{ product.category }}</p>
      <p>Подкатегория: {{ product.subCategory }}</p>
      <p>Название: {{product.name}}</p>
      <p v-if="product.name.length > 30" style="color: red">В названии более 30 символов! Рекомендовано изменить название!</p>
      <p>Проверефицированных товаров данной категории: {{ product.countOfCategoryProducts }}</p>
      <p>ID: {{ product.id }}</p>
    </div>
    <div>
      <h3>Работа с информацией</h3>
      <Button  @click="visibleChangeCategory = true" label="Изменить категорию" style="margin-bottom: 0.5rem;"/>
      <Button  @click="visibleChangeSubCategory = true" label="Изменить подкатегорию"/>
        <Button  @click="deleteFromDB()" label="Удалить из бд"/>
    </div>
    <Dialog v-model:visible="visibleChangeName" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение названия</h3>
        <p>Полное название: {{product.name}}</p>
        <p>Длина названия: {{ product.name.length }}</p>
        <p v-if="product.name.length > 30">Первые 30 символов названия: {{ product.name.slice(0,30) }}</p>
        <InputText type="text" v-model="newName" style="min-width: 300px; margin: 0 1rem 1rem 0"/>
        <Button  label="Сохранить" @click="saveNewName()"/>
      </div>
    </Dialog>

    <Dialog v-model:visible="visibleChangeCategory" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение категории</h3>
        <p>Текущая категория: {{product.category}}</p>
        <InputText type="text" v-model="newCategory" style="min-width: 300px; margin: 0 1rem 1rem 0"/>
        <Button  label="Сохранить" @click="saveNewCategory()"/>
      </div>
    </Dialog>

     <Dialog v-model:visible="visibleChangeSubCategory" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Изменение подкатегории</h3>
        <p>Текущая подкатегория: {{product.subCategory}}</p>
        <InputText type="text" v-model="newSubCategory" style="min-width: 300px; margin: 0 1rem 1rem 0"/>
        <Button  label="Сохранить" @click="saveNewSubCategory()"/>
      </div>
    </Dialog>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Dialog from "primevue/dialog";

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button, InputText, Dialog},
  props: {
    verification: {
      type: Object,
      default: {}
    },
    product: {
      type: Object,
      default: {}
    },
  },
  data() {
    return {
      visibleChangeName: false,
      visibleChangeCategory: false,
      visibleChangeSubCategory: false,
      newName: '',
      newCategory: '',
      newSubCategory: ''
    }
  },
  methods: {
    deleteImage(): void {
      this.product.deleteImage(this.verification.activeIndex)
    },
    saveNewName(): void {
      this.product.saveNewName(this.newName)
      this.visibleChangeName = false
    },
    saveNewSubCategory(): void {
      this.product.saveNewSubCategory(this.newSubCategory)
      this.visibleChangeSubCategory = false
    },
    saveNewCategory(): void {
      this.product.saveNewCategory(this.newCategory)
      this.visibleChangeCategory = false
    },
    saveProduct(): void {
      this.product.saveProduct()
    },
    deleteProduct(): void {
      this.product.deleteProduct()
    },
    deleteFromDB(): void {
        this.product.deleteFromDB()
    }
  },
  updated() {
    if (this.product.name.length > 30) {
      this.newName = this.product.name.slice(0,30)
    }
    else this.newName = this.product.name

    this.newSubCategory = this.product.subCategory

    this.newCategory = this.product.category
  }
})
</script>

<style scoped>
  .p-dialog-header {
    padding: 0 !important;
  }

  .toolbar-block__button {
    margin-right: 1rem;
  }
</style>