import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'

const base_url = import.meta.env.VITE_BASE_URL
export const useAdminPanelStore = defineStore('adminPanel_ozon', {
    state: () => ({
        timesheet: [],
        countOfProductsInCategory: []
    }),
    actions: {
        storeCategory(): void {
            const productStore = useProductStore()
            axios.post(base_url + '/store_category', {
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
            axios.post(base_url + '/return_all_categories')
                .then((response) => {
                    if (response.status == 200){
                        productStore.get_verification_information()
                    }
                })
        },
        getTimeSheet(): void {
            axios.get(base_url + '/get_timesheet')
                .then((response) => {
                    if (response.status == 200){
                        this.timesheet = response.data
                        this.getCountOfProductsInCategory()
                    }
                })
        },
        getCountOfProductsInCategory(): void {
            axios.get(base_url + '/count_of_products_in_category')
                .then((response) => {
                    if (response.status == 200){
                        this.countOfProductsInCategory = response.data
                    }
                })
        },
        getVideos(): void {
             axios.get(base_url + '/create_videos')
                .then((response) => {

                })
        }
    }
})