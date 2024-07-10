<template>
  <div style="display: flex">
    <Galleria :value="images" v-model:activeIndex="activeIndex" :numVisible="4" :circular="true" containerStyle="max-width: 800px; min-width: 600px"
              :showItemNavigators="true">
      <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="display: block; width: 550px" />
      </template>
      <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block; width: 110px" />
      </template>
    </Galleria>

    <div>
      <Button  @click="deleteImage()" label="Удалить"/>
      <Button  label="Кнопка1"/>
      <Button  label="Кнопка2"/>
    </div>
  </div>
</template>

<script lang="ts">
import Galleria from 'primevue/galleria';
import Button from 'primevue/button';

export default {
  name: "GalleryComponent",
  components: {
    Galleria, Button
  },
  data() {
    return {
      images: [],
      activeIndex: 0
    }
  },
  methods: {
    deleteImage(): void {
      this.images.splice(this.activeIndex, 1)
      console.log(this.activeIndex)
    }
  },
  mounted() {
    this.images = [
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-o/7036605492.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-o/7036605492.jpg',
        alt: 'Description for Image 1',
        id: '1'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-l/7048289145.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-l/7048289145.jpg',
        alt: 'Description for Image 1',
        id: '2'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-1/7048289161.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-1/7048289161.jpg',
        alt: 'Description for Image 1',
        id: '3'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-x/7048289121.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-x/7048289121.jpg',
        alt: 'Description for Image 1',
        id: '4'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-h/7048289141.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-h/7048289141.jpg',
        alt: 'Description for Image 1',
        id: '5'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-i/7048289142.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-i/7048289142.jpg',
        alt: 'Description for Image 1',
        id: '6'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-w/7048289048.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-w/7048289048.jpg',
        alt: 'Description for Image 1',
        tid: '7'
      },
      {
        itemImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-8/7048289168.jpg',
        thumbnailImageSrc: 'https://cdn1.ozone.ru/s3/multimedia-1-8/7048289168.jpg',
        alt: 'Description for Image 1',
        id: '8'
      },
    ]
  }
}
</script>

<style scoped>

</style>