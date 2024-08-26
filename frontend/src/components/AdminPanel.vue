<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="goToUrl"/>
  <div class="admin-panel-block">
      <h3>Работа с данными</h3>
      <div>
        <Button label="Отложить текущую категорию товаров" class="admin-panel__button" @click="storeCategory()"/>
        <Button label="Вернуть все отложенные товары" class="admin-panel__button" @click="returnAllCategories()"/>
        <Button label="Создать видео" class="admin-panel__button" @click="getVideos()"/>
      </div>
      <div class="timesheet-and-count-of-products-block">
        <div>
          <h3>Расписание:</h3>
          <div v-for="el in adminPanel.timesheet" style="margin: 1rem">
            <p style="white-space: pre-line">
              {{ el }}
            </p>
          </div>
        </div>
        <div>
          <h3>Кол-во товаров по категориям:</h3>
          <div v-for="el in adminPanel.countOfProductsInCategory" style="margin: 1rem">
            <p>
              {{ el }}
            </p>
          </div>
        </div>
      </div>
  </div>
</template>

<script lang="ts">
import Button from 'primevue/button';
import {defineComponent} from 'vue'
import NavbarComponent from "@/components/NavbarComponent.vue";
import {useAdminPanelStore} from "@/stores/ozon";
import {mapStores} from "pinia";
export default defineComponent({
  name: "AdminPanel",
  props: {
    adminPanel: {
      type: Object,
      default: {}
    },
    goToUrl: {
      type: String,
      default: '/'
    }
  },
  components: {NavbarComponent, Button},
  methods: {
      storeCategory() {
          this.adminPanel.storeCategory()
          this.$router.push(this.goToUrl)
      },
      returnAllCategories() {
          this.adminPanel.returnAllCategories()
          this.$router.push(this.goToUrl)
      },
      getVideos(){
        this.adminPanel.getVideos()
      }
  },
  created() {
    this.adminPanel.getTimeSheet()
  }
})
</script>

<style scoped>
  .admin-panel-block {
    padding: 0 1rem 1rem 1rem;
  }

  .admin-panel__button {
    margin-right: 1rem;
    margin-bottom: 1rem
  }

  .timesheet-and-count-of-products-block{
    display: flex
  }

  @media screen and (max-width: 480px) {
    .admin-panel__button {
      margin-bottom: 0.5rem
    }
    .timesheet-and-count-of-products-block{
      display: block;
    }
    .admin-panel-block {
      padding: 0 0.5rem 0.5rem 0.5rem;
    }
  }
</style>