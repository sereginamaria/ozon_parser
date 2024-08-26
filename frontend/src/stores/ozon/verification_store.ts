import { defineStore } from 'pinia'

export const useVerificationStore = defineStore('verification_ozon', {
    state: () => ({
        activeIndex: 0 as number,
        contentReady: false as boolean,
        contentEmpty: false as boolean,
        images: [] as object[],
    })
})