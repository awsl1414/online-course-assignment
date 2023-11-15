import { createRouter, createWebHashHistory } from "vue-router";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import NotFound from "../views/NotFound.vue";
import Test from "../views/Test.vue";

const routes = [
  // 其中的name属性被官方弃用了
  { path: "/home", component: Home },
  { path: "/login", component: Login },
  { path: "/404", component: NotFound },
  { path: "/test", component: Test },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes: routes,
});

// 导航守卫：全局导航守卫
router.beforeEach((to, form, next) => {
  const token = localStorage.getItem("token");
  if (!token && to.path !== "/login") next("/login");
  else next();
});

export default router;
