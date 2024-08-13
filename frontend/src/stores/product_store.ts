import { defineStore } from 'pinia'
import axios from "axios";
import { useGalleryStore } from './gallery_store'

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

export const useProductStore = defineStore('product', {
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
            const galleryStore = useGalleryStore()
            axios.get(base_url + '/get_verification_information')
                .then ((response) => {
                    let imagesURL: string

                    if (response.data[0] === null) {
                        galleryStore.contentEmpty = true
                        galleryStore.contentReady = false
                    }
                    else {
                        [this.id, this.category, this.subCategory, this.name, this.article, this.price, imagesURL] = response.data[0];
                        this.countOfCategoryProducts = response.data[1][1]

                        this.images = imagesURL.split(', ')

                        galleryStore.images = []
                        let i: number = 0
                        this.images.forEach( (image: string): void => {
                            galleryStore.images.push(
                                {
                                    itemImageSrc: image,
                                    thumbnailImageSrc: image,
                                    alt: 'gallery image',
                                    id: i
                                }
                            )
                            i++
                        })

                        galleryStore.contentReady = true
                        galleryStore.contentEmpty = false
                    }

                })
        },
        deleteImage(activeIndex: number): void {
            const galleryStore = useGalleryStore()
            if (this.images !== null) {
                this.images.splice(activeIndex, 1)
            }
            galleryStore.images.splice(activeIndex, 1)

            if (this.images.length == 3){
                this.images.push(this.images[0])
                galleryStore.images.push(galleryStore.images[0])

            }
        },
        saveNewName(newName: string): void {
            this.name = newName
        },
        saveProduct(): void {
            axios.post(base_url + '/save_product', {
                id: this.id,
                name: this.name,
                images: this.images
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
        }
    },
})