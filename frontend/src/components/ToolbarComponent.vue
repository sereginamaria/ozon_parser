<template>
    <div>
      <Button  @click="deleteImage()" label="Удалить"/>
      <Button  label="Кнопка1"/>
      <Button  label="Кнопка2"/>
    </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Button from 'primevue/button';

export default defineComponent({
  name: "ToolbarComponent",
  components: {Button},
  props: {
    activeIndex: Number
  },
  methods: {
    deleteImage(): void {
      // this.images.splice(this.activeIndex, 1)

      console.log(this.activeIndex)
    }
  }
})
</script>

<style scoped>

</style>