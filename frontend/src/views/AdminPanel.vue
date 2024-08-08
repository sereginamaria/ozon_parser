<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="'/'"/>
  <div>
      <h3>Работа с данными</h3>
      <div>
        <Button  label="Отложить текущую категорию товаров" style="margin-right: 5%" @click="storeCategory()"/>
        <Button  label="Вернуть все отложенные товары" @click="returnAllCategories()"/>
      </div>
      <Button  label="Показать количество проверефецированных товаров" style="margin-top: 1%" @click="getCountOfCategories()"/>
      <div v-for="el in adminPanel.list">
          <p>
            {{ el }}
          </p>
      </div>
  </div>
</template>

<script lang="ts">
import Button from 'primevue/button';
import {defineComponent} from 'vue'
import NavbarComponent from "@/components/NavbarComponent.vue";
import {useAdminPanelStore} from "@/stores";
import {mapStores} from "pinia";
export default defineComponent({
  name: "AdminPanel",
  components: {NavbarComponent, Button},
  computed: {
      ...mapStores(useAdminPanelStore),
  },
  methods: {
      storeCategory() {
          this.adminPanel.storeCategory()
          this.$router.push('/')
      },
      returnAllCategories() {
          this.adminPanel.returnAllCategories()
          this.$router.push('/')
      },
      getCountOfCategories() {
          this.adminPanel.getCountOfCategories()
      }
  }
})
</script>

<style scoped>

</style>