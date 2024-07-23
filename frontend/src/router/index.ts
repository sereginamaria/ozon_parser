import { createRouter, createWebHashHistory } from "vue-router"

import VerificationView from '../views/Verification.vue'
import AdminPanel from "@/views/AdminPanel.vue";

const routes = [
	{
		path: "/",
		name: "verification",
		component: VerificationView
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