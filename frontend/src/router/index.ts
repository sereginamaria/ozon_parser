import { createRouter, createWebHashHistory } from "vue-router"

import Auth from "@/views/Auth.vue";
import Home from "@/views/Home.vue"
import OzonVerification from "@/views/ozon/OzonVerification.vue";
import OzonAdminPanel from "@/views/ozon/OzonAdminPanel.vue";
import WbAdminPanel from "@/views/wb/WbAdminPanel.vue";
import WbVerification from "@/views/wb/WbVerification.vue";

const routes = [
	{
		path: "/",
		name: "Auth",
		component: Auth
	},
	{
		path: "/home",
		name: "Home",
		component: Home
	},
	{
		path: "/ozon/verification",
		name: "OzonVerification",
		component: OzonVerification
	},
	{
		path: "/ozon/admin-panel",
		name: "OzonAdminPanel",
		component: OzonAdminPanel
	},
	{
		path: "/wb/verification",
		name: "WbVerification",
		component: WbVerification
	},
	{
		path: "/wb/admin-panel",
		name: "WbAdminPanel",
		component: WbAdminPanel
	}
]


export const router = createRouter({
	history: createWebHashHistory(),
	routes: routes
})

router.beforeEach((to, from, next) => {
	if (to.name !== 'Auth' && localStorage.getItem('isAuth') === 'false') next({ name: 'Auth' })
	else next()
})

