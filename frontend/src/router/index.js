import login from "../components/Login.vue";
import work from "../components/work.vue";
import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/login", name: "login", component: login },

  { path: "/work", name: "work", component: work },

  {
    path: "/:pathMatch(.*)*",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
export default router;
