import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from 'axios'
// import { createPinia, setActivePinia } from 'pinia';
// setActivePinia(createPinia());
const base_url = import.meta.env.VITE_BASE_URL

interface State {
    contentReady: boolean,
    products: Array<Product>
}

interface Product {
    sub_category: string;
    article: string;
    price: number,
    images: string[],
    imagesIndex: number[]
}

export const useStylistPanelStore = defineStore('stylistPanel_wb', {
    state: () => ({
        contentReady: false,
        products: [],
        imagesIndex: [0, 0, 0, 0]
    }),
    actions: {
        get_stylist_panel_information() {
            const productStore = useProductStore()
            axios.get(base_url + '/wb/get_stylist_card_information')
                .then ((response) => {
                    this.contentReady = false
                    this.products = []

                    console.log('wb')
                    console.log(response.data)
                    console.log(response.data[0].article)
                    if (response.data[0] === null) {
                        this.contentReady = false
                    }
                    else {
                        response.data.forEach((product: object):void => {
                            console.log(response.data.indexOf(product))
                            console.log(product)
                            let index = response.data.indexOf(product)
                            this.products.push({
                                sub_category: product.sub_category,
                                article: product.article,
                                price: product.price,
                                images: product.images.split(', '),
                            })

                            console.log(this.products)
                        })

                        this.contentReady = true
                    }
                })
        },
        saveStyledCard(){
            console.log(this.products)
            axios.post(base_url + '/wb/save_styled_card', {
                products: this.products
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_stylist_panel_information()
                    }
                })
        },
        deleteStyledCard(){
            this.get_stylist_panel_information()
        }
    }
})