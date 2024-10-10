import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import { useVerificationStore } from "./verification_store";
import axios from 'axios'
import { createPinia, setActivePinia } from 'pinia';
setActivePinia(createPinia());

const base_url = import.meta.env.VITE_BASE_URL
const productStore = useProductStore()
const verificationStore = useVerificationStore()

export const useAdminPanelStore = defineStore('adminPanel_wb', {
    state: () => ({
        timesheet: [],
        countOfVerifiedProducts: [],
        countOfNotVerifiedProducts: []
    }),
    actions: {
        storeCategory(): void {
            axios.post(base_url + '/wb/store_category', {
                category: productStore.category
            })
                .then((response) => {
                    if (response.status == 200){
                        verificationStore.get_verification_information()
                    }
                })
        },
        returnAllCategories(): void {
            axios.post(base_url + '/wb/return_all_categories')
                .then((response) => {
                    if (response.status == 200){
                        verificationStore.get_verification_information()
                    }
                })
        },
        getTimeSheet(): void {
            axios.get(base_url + '/wb/get_timesheet')
                .then((response) => {
                    if (response.status == 200){
                        this.timesheet = response.data
                        this.getCountOfVerifiedProducts()
                    }
                })
        },
        getCountOfVerifiedProducts(): void {
            axios.get(base_url + '/wb/count_of_verified_products')
                .then((response) => {
                    if (response.status == 200){
                        this.countOfVerifiedProducts = response.data
                        this.getCountOfNotVerifiedProducts()
                    }
                })
        },
        getCountOfNotVerifiedProducts(): void {
            axios.get(base_url + '/wb/count_of_not_verified_products')
                .then((response) => {
                    if (response.status == 200){
                        this.countOfNotVerifiedProducts = response.data
                    }
                })
        },
        getVideos(): void {
             axios.get(base_url + '/wb/create_videos')
                .then((response) => {

                })
        }
    }
})