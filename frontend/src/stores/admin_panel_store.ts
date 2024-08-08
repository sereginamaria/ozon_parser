import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'
export const useAdminPanelStore = defineStore('adminPanel', {
    state: () => ({
        list: []
    }),
    actions: {
        storeCategory(): void {
            const productStore = useProductStore()
            axios.post('http://127.0.0.1:5000/store_category', {
                category: productStore.category
            })
                .then((response) => {
                    if (response.status == 200){
                        productStore.get_verification_information()
                    }
                })
        },
        returnAllCategories(): void {
            const productStore = useProductStore()
            axios.post('http://127.0.0.1:5000/return_all_categories')
                .then((response) => {
                    if (response.status == 200){
                        productStore.get_verification_information()
                    }
                })
        },
        getCountOfCategories(): void {
            axios.get('http://127.0.0.1:5000/get_count_of_categories')
                .then((response) => {
                    this.list = response.data
                })
        }
    }
})