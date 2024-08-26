import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'

const base_url = import.meta.env.VITE_BASE_URL
export const useAdminPanelStore = defineStore('adminPanel_ozon', {
    state: () => ({
        timesheet: [],
        countOfVerifiedProducts: [],
        countOfNotVerifiedProducts: []
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
                        this.getCountOfVerifiedProducts()
                        this.getCountOfNotVerifiedProducts()
                    }
                })
        },
        getCountOfVerifiedProducts(): void {
            axios.get(base_url + '/count_of_verified_products')
                .then((response) => {
                    if (response.status == 200){
                        this.countOfVerifiedProducts = response.data
                    }
                })
        },
        getCountOfNotVerifiedProducts(): void {
            axios.get(base_url + '/count_of_not_verified_products')
                .then((response) => {
                    if (response.status == 200){
                        this.countOfNotVerifiedProducts = response.data
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