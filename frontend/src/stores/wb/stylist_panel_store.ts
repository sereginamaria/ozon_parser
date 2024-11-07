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
    product_category: string;
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
                                product_category: product.publication_category,
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
            console.log(this.imagesIndex)

            this.imagesIndex.forEach((item, index, theArray) => {
                if (item !== 0){
                    console.log('indexof index')
                    console.log(index)
                    console.log(this.products[index])
                    console.log(this.products[index].images[0])

                    console.log(this.products[index].images[item])
                    this.products[index].images.unshift(...this.products[index].images.splice(item,1));
                    console.log(this.products[index].images[0])

                    theArray[index] = 0
                    console.log(this.imagesIndex)

                }
            })
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
        },
        changeImage(n:number){
            axios.get(base_url + '/wb/change_stylist_panel_image/' + this.products[n].product_category)
                .then ((response) => {
                    if (response.status == 200){
                        console.log('ddddddddddddd')
                        console.log(response.data[0])
                        this.products.splice(n, 1,
                            {
                                sub_category: response.data[0].sub_category,
                                article: response.data[0].article,
                                price: response.data[0].price,
                                product_category: response.data[0].publication_category,
                                images: response.data[0].images.split(', '),
                            })


                        // this.products[n]
                    }
                })
        }
    }
})