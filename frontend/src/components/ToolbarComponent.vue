<template>
  <div>
      <div>
        <p>Работа с изображениями</p>
        <Button  @click="deleteImage()" label="Удалить"/>
      </div>
      <div>
        <p>Оставляем товар?</p>
        <Button  label="Да"/>
        <Button  label="Нет"/>
      </div>
      <div>
        <p>Изменить имя</p>
        <Button  label="Да"/>
        <Button  label="Нет"/>
      </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import { mapStores } from 'pinia'
import { useGalleryStore } from '@/stores';

import Button from 'primevue/button';

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button},
  computed: {
    ...mapStores(useGalleryStore),
  },
  methods: {
    deleteImage(): void {
      // this.images.splice(this.activeIndex, 1)

      console.log(this.gallery.activeIndex)
    }
  }
})
</script>

<style scoped>

</style>