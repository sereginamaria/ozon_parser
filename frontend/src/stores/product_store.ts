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
    images: string[]
}
export const useProductStore = defineStore('product', {
    state: (): State  => {
        return  {
            id:  0,
            category: '',
            subCategory: '',
            name: '',
            article: '',
            price: '',
            images: []
        }
    },
    actions: {
        get_verification_information() {
            const galleryStore = useGalleryStore()
            axios.get('http://127.0.0.1:5000/get_verification_information')
                .then ((response) => {
                    let imagesURL: string
                    [this.id, this.category, this.subCategory, this.name, this.article, this.price, imagesURL] = response.data;

                    this.images = imagesURL.split(',')

                    galleryStore.images = []
                    this.images.forEach( (image: string): void => {
                        let i: number = 0
                        galleryStore.images.push(
                            {
                                itemImageSrc: image,
                                thumbnailImageSrc: image,
                                alt: 'gallery image',
                                id: i
                            }
                        )
                    })

                    galleryStore.contentReady = true
                })
        },
        deleteImage(activeIndex: number): void {
            const galleryStore = useGalleryStore()
            if (this.images !== null) {
                this.images.splice(activeIndex, 1)
            }
            galleryStore.images.splice(activeIndex, 1)
        },
        saveNewName(newName: string): void {
            this.name = newName
        },
        saveProduct(): void {
            axios.post('http://127.0.0.1:5000/save_product', {
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
            axios.post('http://127.0.0.1:5000/delete_product', {
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