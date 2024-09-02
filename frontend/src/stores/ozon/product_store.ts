import { defineStore } from 'pinia'
import axios from "axios";
import { useVerificationStore } from './verification_store'

interface State {
    id?: number,
    category: string,
    subCategory: string,
    name: string,
    article: string,
    price: string,
    images: string[],
    countOfCategoryProducts: number
}

const base_url = import.meta.env.VITE_BASE_URL

export const useProductStore = defineStore('product_ozon', {
    state: (): State  => {
        return  {
            id:  0,
            category: '',
            subCategory: '',
            name: '',
            article: '',
            price: '',
            images: [],
            countOfCategoryProducts: 0
        }
    },
    actions: {
        get_verification_information() {
            const verificationStore = useVerificationStore()
            axios.get(base_url + '/get_verification_information')
                .then ((response) => {
                    let imagesURL: string

                    if (response.data[0] === null) {
                        verificationStore.contentEmpty = true
                        verificationStore.contentReady = false
                    }
                    else {
                        [this.id, this.category, this.subCategory, this.name, this.article, this.price, imagesURL] = response.data[0];
                        this.countOfCategoryProducts = response.data[1][0]

                        this.images = imagesURL.split(', ')

                        verificationStore.images = []
                        let i: number = 0
                        this.images.forEach( (image: string): void => {
                            verificationStore.images.push(
                                {
                                    itemImageSrc: image,
                                    thumbnailImageSrc: image,
                                    alt: 'gallery image',
                                    id: i
                                }
                            )
                            i++
                        })

                        verificationStore.contentReady = true
                        verificationStore.contentEmpty = false
                    }

                })
        },
        deleteImage(activeIndex: number): void {
            const verificationStore = useVerificationStore()
            if (this.images !== null) {
                this.images.splice(activeIndex, 1)
            }
            verificationStore.images.splice(activeIndex, 1)

            if (this.images.length == 3){
                this.images.push(this.images[0])
                verificationStore.images.push(verificationStore.images[0])

            }
        },
        saveNewName(newName: string): void {
            this.name = newName
        },
        saveNewSubCategory(NewSubCategory: string): void {
            this.subCategory = NewSubCategory
        },
        saveNewCategory(newCategory: string): void {
            this.category = newCategory
        },
        saveProduct(): void {
            axios.post(base_url + '/save_product', {
                id: this.id,
                name: this.name,
                images: this.images,
                sub_category: this.subCategory,
                category: this.category
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteProduct(): void {
            axios.post(base_url + '/delete_product', {
                id: this.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteFromDB(): void {
            axios.post(base_url + '/delete_product_from_db', {
                id: this.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        }
    },
})