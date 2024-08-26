<template>
  <NavbarComponent :label="'Верификация'" :goToUrl="goToUrl"/>
  <div class="admin-panel-block">
      <h3>Работа с данными</h3>
      <div>
        <Button label="Отложить текущую категорию товаров" class="admin-panel__button" @click="storeCategory()"/>
        <Button label="Вернуть все отложенные товары" class="admin-panel__button" @click="returnAllCategories()"/>
        <Button label="Создать видео" class="admin-panel__button" @click="getVideos()"/>
      </div>
<!--      <div class="timesheet-and-count-of-products-block">-->
         <Accordion :value="['0','1', '2']" multiple class="timesheet-and-count-of-products-block">
            <AccordionPanel value="0">
              <AccordionHeader>
                <h3 style="margin-right: 1rem;">Расписание:</h3>
              </AccordionHeader>
              <AccordionContent>
                <div v-for="el in adminPanel.timesheet" style="margin: 1rem">
                  <p style="white-space: pre-line">
                    {{ el }}
                  </p>
                </div>
              </AccordionContent>
            </AccordionPanel>
            <AccordionPanel value="1">
              <AccordionHeader>
                <h3 style="margin-right: 1rem;">Кол-во проверифицированных товаров:</h3>
              </AccordionHeader>
              <AccordionContent>
                <div v-for="el in adminPanel.countOfVerifiedProducts" style="margin: 1rem">
                  <p>
                    {{ el }}
                  </p>
                </div>
              </AccordionContent>
            </AccordionPanel>
            <AccordionPanel value="2">
              <AccordionHeader>
                <h3 style="margin-right: 1rem;">Кол-во непроверифицированных товаров:</h3>
              </AccordionHeader>
              <AccordionContent>
                <div v-for="el in adminPanel.countOfNotVerifiedProducts" style="margin: 1rem">
                  <p>
                    {{ el }}
                  </p>
                </div>
              </AccordionContent>
            </AccordionPanel>
         </Accordion>

<!--        <div>-->
<!--          <h3>Расписание:</h3>-->
<!--          <div v-for="el in adminPanel.timesheet" style="margin: 1rem">-->
<!--            <p style="white-space: pre-line">-->
<!--              {{ el }}-->
<!--            </p>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div>-->
<!--          <h3>Кол-во проверифицированных товаров:</h3>-->
<!--          <div v-for="el in adminPanel.countOfVerifiedProducts" style="margin: 1rem">-->
<!--            <p>-->
<!--              {{ el }}-->
<!--            </p>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div>-->
<!--          <h3>Кол-во непроверифицированных товаров:</h3>-->
<!--          <div v-for="el in adminPanel.countOfNotVerifiedProducts" style="margin: 1rem">-->
<!--            <p>-->
<!--              {{ el }}-->
<!--            </p>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
  </div>
</template>

<script lang="ts">
import Button from 'primevue/button';
import {defineComponent} from 'vue'
import NavbarComponent from "@/components/NavbarComponent.vue";
import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';

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
  components: {NavbarComponent, Button, Accordion, AccordionPanel, AccordionHeader, AccordionContent},
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
  .timesheet-and-count-of-products-block div{
    padding: 0 1rem;
  }


  @media screen and (max-width: 480px) {
    .admin-panel__button {
      margin-bottom: 0.5rem
    }
    .timesheet-and-count-of-products-block{
      display: block;
    }
    .timesheet-and-count-of-products-block div{
      padding: 0;
    }
    .admin-panel-block {
      padding: 0 0.5rem 0.5rem 0.5rem;
    }
  }
</style>