import './assets/main.css'
import './assets/galleria.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { router } from './router'

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';


const pinia = createPinia()
const app = createApp(App);


app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

app.use(pinia)
app.use(router)

app.mount('#app')
