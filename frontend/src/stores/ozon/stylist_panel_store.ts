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
    images: string[]
}

export const useStylistPanelStore = defineStore('stylistPanel_ozon', {
    state: () => ({
        contentReady: false,
        products: []
    }),
    actions: {
        get_stylist_panel_information() {
            const productStore = useProductStore()
            axios.get(base_url + '/get_stylist_card_information')
                .then ((response) => {
                    this.contentReady = false
                    this.products = []

                    console.log('ozon')
                    console.log(response.data)
                    console.log(response.data[0].article)

                    if (response.data[0] === null) {
                        this.contentReady = false
                    }
                    else {
                        this.products = []
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
            axios.post(base_url + '/save_styled_card', {
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