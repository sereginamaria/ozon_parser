import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', {
    state: () => ({
        id: 0,
        category: 'Категория',
        subCategory: 'Подкатегория',
        name: 'Название',
        article: 'Артикул',
        price: 'Цена',
        images: [
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
    }),
    getters: {

    },
    actions: {

    },
})