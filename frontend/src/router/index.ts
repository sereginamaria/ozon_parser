import { createRouter, createWebHashHistory } from "vue-router"

import Verification from '@/views/Verification.vue'
import AdminPanel from "@/views/AdminPanel.vue";
import Auth from "@/views/Auth.vue";

const routes = [
	{
		path: "/",
		name: "Auth",
		component: Auth
	},
	{
		path: "/verification",
		name: "Verification",
		component: Verification
	},
	{
		path: "/admin-panel",
		name: "AdminPanel",
		component: AdminPanel
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

