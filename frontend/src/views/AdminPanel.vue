<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="'/'"/>
  <div>
      <h3>Работа с данными</h3>
      <div>
        <Button  label="Отложить текущую категорию товаров" style="margin-right: 5%" @click="storeCategory()"/>
        <Button  label="Вернуть все отложенные товары" @click="returnAllCategories()"/>
      </div>
      <Button  label="Показать расписание" style="margin-top: 1%"/>
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
      }
  }
})
</script>

<style scoped>

</style>