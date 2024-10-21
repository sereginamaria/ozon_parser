import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'
import { createPinia, setActivePinia } from 'pinia';
setActivePinia(createPinia());
const base_url = import.meta.env.VITE_BASE_URL


export const useStylistPanelStore = defineStore('stylistPanel_wb', {
    state: () => ({
        contentReady: false,
        products: []
    }),
    actions: {
        get_stylist_panel_information() {
            const productStore = useProductStore()
            axios.get(base_url + '/wb/get_stylist_card_information')
                .then ((response) => {
                    console.log(response.data)
                    console.log(response.data[0].article)
                    let imagesURL: string

                    if (response.data[0] === null) {
                        this.contentReady = false
                    }
                    else {
                        response.data.forEach(product => {
                            console.log(response.data.indexOf(product))
                            console.log(product)
                            let index = response.data.indexOf(product)
                            this.products.push({
                                index: {}
                            })
                        })

                        // [productStore.id, productStore.category, productStore.subCategory,
                        //     productStore.name, productStore.article, productStore.price, imagesURL] = response.data[0];
                        //
                        // productStore.images = imagesURL.split(', ')
                        //
                        // productStore.images = []
                        // let i: number = 0
                        // productStore.images.forEach( (image: string): void => {
                        //     this.images.push(
                        //         {
                        //             itemImageSrc: image,
                        //             thumbnailImageSrc: image,
                        //             alt: 'gallery image',
                        //             id: i
                        //         }
                        //     )
                        //     i++
                        // })
                        //
                        // this.contentReady = true
                        // this.contentEmpty = false
                    }
                })
        },
    }
})