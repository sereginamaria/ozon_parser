import { defineStore } from 'pinia'

export const useGalleryStore = defineStore('gallery', {
    state: () => ({
        activeIndex: 0 as number,
        contentReady: false as boolean,
        contentEmpty: false as boolean,
        images: [] as object[],
    })
})