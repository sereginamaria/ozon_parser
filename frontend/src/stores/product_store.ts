import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', {
    state: () => ({
        id: 0,
        category: 'Категория',
        subCategory: 'Подкатегория',
        name: 'Название'
    }),
    getters: {

    },
    actions: {

    },
})