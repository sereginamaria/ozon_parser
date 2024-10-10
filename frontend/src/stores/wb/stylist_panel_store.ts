import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'
import { createPinia, setActivePinia } from 'pinia';
setActivePinia(createPinia());
const base_url = import.meta.env.VITE_BASE_URL
const productStore = useProductStore()

export const useStylistPanelStore = defineStore('stylistPanel_wb', {
    state: () => ({
        productStore: useProductStore(),
        contentReady: true
    }),
    actions: {
        get_stylist_panel_information() {
            axios.get(base_url + '/wb/get_stylist_card_information')
                .then ((response) => {
                    console.log(response.data)
                    let imagesURL: string

                    // if (response.data[0] === null) {
                    //     this.contentReady = false
                    // }
                    // else {
                    //     [productStore.id, productStore.category, productStore.subCategory,
                    //         productStore.name, productStore.article, productStore.price, imagesURL] = response.data[0];
                    //
                    //     productStore.images = imagesURL.split(', ')
                    //
                    //     productStore.images = []
                    //     let i: number = 0
                    //     productStore.images.forEach( (image: string): void => {
                    //         this.images.push(
                    //             {
                    //                 itemImageSrc: image,
                    //                 thumbnailImageSrc: image,
                    //                 alt: 'gallery image',
                    //                 id: i
                    //             }
                    //         )
                    //         i++
                    //     })
                    //
                    //     this.contentReady = true
                    //     this.contentEmpty = false
                    // }
                })
        },
    }
})