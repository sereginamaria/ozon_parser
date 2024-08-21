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
          this.adminPanel.getTimeSheet()

          console.log(this.adminPanel.list)
          console.log(typeof this.adminPanel.list)

          this.adminPanel.list.forEach((el) => {
            console.log(el)
            console.log(typeof el)
            console.log(el[0])
            console.log(el[1])

          })


        let timesheet = {
          'Monday': {
              "Украшения": '6:00',
              "Верхняя Одежда": '8:00',
              "Кофта": '10:00',
              "Брюки": '12:00',
              "Джинсы": '14:00',
              "Платье": '16:00',
              "Пиджак": '18:00',
              "Сумка": '20:00',
          },
          'Tuesday': {
              "Аксессуары": '6:00',
              "Шорты": '8:00',
              "Пиджак": '10:00',
              "Кофта": '12:00',
              "Костюм": '14:00',
              "Юбка": '16:00',
              "Блузка": '18:00',
              "Обувь": '20:00',
          },
          'Wednesday': {
              "Украшения": '6:00',
              "Верхняя Одежда": '8:00',
              "Кофта": '10:00',
              "Футболка": '12:00',
              "Пиджак": '14:00',
              "Брюки": '16:00',
              "Топ": '18:00',
              "Сумка": '20:00',
          },
          'Thursday': {
              "Аксессуары": '6:00',
              "Корсет": '8:00',
              "Костюм": '10:00',
              "Юбка": '12:00',
              "Рубашка": '14:00',
              "Джинсы": '16:00',
              "Футболка": '18:00',
              "Обувь": '20:00',
          },
          'Friday': {
              "Украшения": '6:00',
              "Верхняя Одежда": '8:00',
              "Кофта": '10:00',
              "Брюки": '12:00',
              "Обувь": '14:00',
              "Топ": '16:00',
              "Платье": '18:00',
              "Сумка": '20:00',
          },
          'Saturday': {
              "Домашняя Одежда": '6:00',
              "Верхняя Одежда": '8:00',
              "Рубашка": '10:00',
              "Джинсы": '12:00',
              "Футболка": '14:00',
              "Пиджак": '16:00',
              "Брюки": '18:00',
              "Обувь": '20:00',
          },
          'Sunday': {
              "Украшения": '6:00',
              "Верхняя Одежда": '8:00',
              "Кофта": '10:00',
              "Блузка": '12:00',
              "Платье": '14:00',
              "Костюм": '16:00',
              "Юбка": '18:00',
              "Сумка": '20:00',
          }
      }

        const date = new Date();
        const options = { weekday: 'long' };
        const dayOfWeek = date.toLocaleString('en-US', options);

        console.log(dayOfWeek);

        let time_array = ['6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']

      }
  },
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