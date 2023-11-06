import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import router from "./router/index.js";

const app = createApp(App);
app.use(router);
app.config.warnHandler = () => null;
app.use(ElementPlus); //在挂载app之前使用ElementPlus
app.mount("#app");
