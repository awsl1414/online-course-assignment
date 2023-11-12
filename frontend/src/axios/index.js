import axios from "axios";

const instance = axios.create({
  baseURL: "http://49.235.107.169:5000/",
  timeout: 2000,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
  },
});
// 添加请求拦截器
instance.interceptors.request.use(
  (config) => {
    // 在请求发送之前做一些处理
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
// 添加响应拦截器
instance.interceptors.response.use(
  (config) => {
    return config;
  },
  (error) => {
    // 错误处理
    return Promise.reject(error);
  }
);

export default instance;
