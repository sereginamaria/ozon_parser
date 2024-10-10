import { defineStore } from 'pinia'

interface State {
    id?: number,
    category: string,
    subCategory: string,
    name: string,
    article: string,
    price: string,
    images: string[]
}

export const useProductStore = defineStore('product_wb', {
    state: (): State  => {
        return  {
            id:  0,
            category: '',
            subCategory: '',
            name: '',
            article: '',
            price: '',
            images: []
        }
    }
})