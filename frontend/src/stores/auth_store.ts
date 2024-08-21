import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
    }),
    actions: {
        auth(login: string, password: string): boolean {
            if (login === 'masha' && password === 'masha') {
                localStorage.setItem('isAuth', 'true');
                return true
            }
            else {
                localStorage.setItem('isAuth', 'false');
                return false
            }
        }
    }
})