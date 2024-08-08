import { createRouter, createWebHashHistory } from "vue-router"

import Verification from '@/views/Verification.vue'
import AdminPanel from "@/views/AdminPanel.vue";

const routes = [
	{
		path: "/",
		name: "verification",
		component: Verification
	},
	{
		path: "/admin-panel",
		name: "admin-panel",
		component: AdminPanel
	}
]

export const router = createRouter({
	history: createWebHashHistory(),
	routes: routes
})