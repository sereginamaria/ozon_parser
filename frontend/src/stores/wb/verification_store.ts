import { defineStore } from 'pinia'
import { useProductStore } from './product_store'
import axios from "axios";

// import { createPinia, setActivePinia } from 'pinia';
// setActivePinia(createPinia());

interface State {
    activeIndex: number,
    contentReady: boolean,
    contentEmpty: boolean,
    images: object[],
    countOfCategoryProducts: number
}

const base_url = import.meta.env.VITE_BASE_URL

// const productStore = useProductStore()

export const useVerificationStore = defineStore('verification_wb', {
    state: () => ({
        activeIndex: 0,
        contentReady: false,
        contentEmpty: false,
        images: [],
        countOfCategoryProducts: 0,

        productStore: useProductStore()
    }),
    actions: {
        get_verification_information() {
            axios.get(base_url + '/wb/get_verification_information')
                .then ((response) => {
                    let imagesURL: string

                    if (response.data[0] === null) {
                        this.contentEmpty = true
                        this.contentReady = false
                    }
                    else {
                        [productStore.id, productStore.category, productStore.subCategory,
                            productStore.name, productStore.article, productStore.price, imagesURL] = response.data[0];
                        this.countOfCategoryProducts = response.data[1][0]

                        productStore.images = imagesURL.split(', ')

                        this.images = []
                        let i: number = 0
                        productStore.images.forEach( (image: string): void => {
                            this.images.push(
                                {
                                    itemImageSrc: image,
                                    thumbnailImageSrc: image,
                                    alt: 'gallery image',
                                    id: i
                                }
                            )
                            i++
                        })

                        this.contentReady = true
                        this.contentEmpty = false
                    }
                })
        },
        deleteImage(activeIndex: number): void {
            if (productStore.images !== null) {
                productStore.images.splice(activeIndex, 1)
            }
            this.images.splice(activeIndex, 1)

            if (productStore.images.length == 3){
                productStore.images.push(productStore.images[0])
                this.images.push(this.images[0])
            }
        },
        saveNewName(newName: string): void {
            productStore.name = newName
        },
        saveNewSubCategory(NewSubCategory: string): void {
            productStore.subCategory = NewSubCategory
        },
        saveNewCategory(newCategory: string): void {
            productStore.category = newCategory
        },
        saveProduct(): void {

            axios.post(base_url + '/wb/save_product', {
                id: productStore.id,
                name: productStore.name,
                images: productStore.images,
                sub_category: productStore.subCategory,
                category: productStore.category
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteProduct(): void {
            axios.post(base_url + '/wb/delete_product', {
                id: productStore.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteFromDB(): void {
            axios.post(base_url + '/wb/delete_product_from_db', {
                id: productStore.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        }
    },
})