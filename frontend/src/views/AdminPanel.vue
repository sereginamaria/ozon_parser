<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="'/verification'"/>
  <div>
      <h3>Работа с данными</h3>
      <div>
        <Button label="Отложить текущую категорию товаров" class="admin-panel__button" @click="storeCategory()"/>
        <Button label="Вернуть все отложенные товары" class="admin-panel__button" @click="returnAllCategories()"/>
      </div>
      <Button  label="Показать количество проверефецированных товаров" class="admin-panel__button" @click="getCountOfCategories()"/>
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
          this.$router.push('/verification')
      },
      returnAllCategories() {
          this.adminPanel.returnAllCategories()
          this.$router.push('/verification')
      },
      getCountOfCategories() {
          this.adminPanel.getCountOfCategories()
      }
  }
})
</script>

<style scoped>
  .admin-panel__button {
    margin-right: 1rem;
    margin-bottom: 1rem
  }

  @media screen and (max-width: 480px) {
    .admin-panel__button {
      margin-bottom: 0.5rem
    }
  }
</style>