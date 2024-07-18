import { createRouter, createWebHashHistory } from "vue-router"

import HomeView from '../views/Home.vue'
import VerificationView from '../views/Verification.vue'

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView
	},
	{
		path: "/verification",
		name: "verification",
		component: VerificationView
	}
]

export const router = createRouter({
	history: createWebHashHistory(),
	routes: routes
})