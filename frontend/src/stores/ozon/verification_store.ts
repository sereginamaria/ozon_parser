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
    countOfCategoryProducts: number,
    listOfSubCategories: string[]
}


const base_url = import.meta.env.VITE_BASE_URL
// const productStore = useProductStore()

export const useVerificationStore = defineStore('verification_ozon', {
    state: () => ({
        activeIndex: 0,
        contentReady: false,
        contentEmpty: false,
        images: [],
        countOfCategoryProducts: 0,

        listOfSubCategories: ['Казаки', 'Куртка', 'Браслет', 'Ремень', 'Воротник', 'Болеро', 'Косынка', 'Кулон',
            'Фуражка', 'Повязка', 'Полупальто', 'Берет', 'Косуха', 'Сумка', 'Комплект', 'Штаны', 'Водолазка',
            'Цепочка', 'Шуба', 'Пижама', 'Майка', 'Дублёнка', 'Ботинки', 'Серьги', 'Юбка', 'Балаклава', 'Кепка',
            'Ботфорты', 'Платье', 'Туфли', 'Плащ', 'Пояс', 'Кольцо', 'Слейв', 'Пуловер', 'Капор', 'Пуховик', 'Набор',
            'Чепчик', 'Сабо', 'Галстук', 'Шапка', 'Жилетка', 'Бант', 'Кардиган', 'Джеггинсы', 'Футболка', 'Свитер',
            'Кроссовки', 'Жакет', 'Корсет', 'Кеды', 'Бусы', 'Тапочки', 'Палантин', 'Бейсболка', 'Топ',
            'Халат', 'Кепи', 'Бодичейн', 'Худи', 'Костюм', 'Жилет', 'Чокер', 'Ушанка', 'Платок', 'Ободок', 'Лонгслив',
            'Джемпер', 'Челси', 'Колье', 'Часы', 'Ветровка', 'Кофта', 'Тренчкот', 'Ботильоны', 'Сарафан', 'Лоферы',
            'Крабик', 'Тельняшка', 'Шоппер', 'Клатч', 'Тренч', 'Подвеска', 'Дутики', 'Ожерелье', 'Толстовка',
            'Полуботинки', 'Рубашка', 'Водолазка', 'Свитшот', 'Брошь', 'Боди', 'Дубленка', 'Брюки', 'Парео',
            'Джинсы', 'Бомбер', 'Пиджак', 'Джоггеры', 'Пальто', 'Блузка'],
        productStore: useProductStore()
    }),
    actions: {
        get_verification_information() {
            axios.get(base_url + '/ozon/get_verification_information')
                .then ((response) => {
                    let imagesURL: string

                    if (response.data[0] === null) {
                        this.contentEmpty = true
                        this.contentReady = false
                    }
                    else {
                        [this.productStore.id, this.productStore.category, this.productStore.subCategory,
                            this.productStore.name, this.productStore.article, this.productStore.price, imagesURL] = response.data[0];
                        this.countOfCategoryProducts = response.data[1][0]

                        this.productStore.images = imagesURL.split(', ')

                        this.images = []
                        let i: number = 0
                        this.productStore.images.forEach( (image: string): void => {
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
            if (this.productStore.images !== null) {
                this.productStore.images.splice(activeIndex, 1)
            }
            this.images.splice(activeIndex, 1)

            if (this.productStore.images.length == 3){
                this.productStore.images.push(this.productStore.images[0])
                this.images.push(this.images[0])
            }
        },
        saveNewName(newName: string): void {
            this.productStore.name = newName
        },
        saveNewSubCategory(NewSubCategory: string): void {
            this.productStore.subCategory = NewSubCategory
        },
        saveNewCategory(newCategory: string): void {
            this.productStore.category = newCategory
        },
        saveProduct(): void {
            axios.post(base_url + '/ozon/save_product', {
                id: this.productStore.id,
                name: this.productStore.name,
                images: this.productStore.images,
                sub_category: this.productStore.subCategory,
                category: this.productStore.category
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteProduct(): void {
            axios.post(base_url + '/ozon/delete_product', {
                id: this.productStore.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        },
        deleteFromDB(): void {
            axios.post(base_url + '/ozon/delete_product_from_db', {
                id: this.productStore.id
            })
                .then ((response) => {
                    if (response.status == 200){
                        this.get_verification_information()
                    }
                })
        }
    },
})