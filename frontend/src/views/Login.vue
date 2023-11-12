<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="welcome-title">欢迎登录</h2>
      <el-form
        :model="form"
        ref="loginForm"
        label-width="80px"
        class="login-form"
      >
        <el-form-item label="用户名" prop="username">
          <el-input
            v-model="form.username"
            placeholder="请输入用户名"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            type="password"
            v-model="form.password"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
      </el-form>
      <div>
        <el-button type="primary" @click="login" class="login-button"
          >登录</el-button
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "../axios/index.js";
import { useRouter } from "vue-router";
import { ref } from "vue";

const TOKENURL = "api/v1/login";

const form = ref({
  username: "",
  password: "",
});
const router = useRouter();
const login = () => {
  axios.post(`${TOKENURL}`, form.value).then((res) => {
    if (res.data.code != 200) alert("账号或密码错误");
    else {
      console.log(res.data.token);
      localStorage.setItem("token", res.data.token);
      //  <script setup> 语法时，this 不再指向组件实例
      // this.$router.push("/home");
      router.push("/home");
    }
  });
};
</script>

<style scoped>
.login-container {
  background-image: url("@/assets/login-bg.jpg");
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.welcome-title {
  font-size: 32px;
  color: #333;
  margin-bottom: 20px;
}

.login-form {
  margin-top: 20px;
  /* 修改输入框长短 */
  width: 355px;
}

.login-button:hover {
  background-color: #1784ba; /* 悬停时颜色更深 */
}
.login-card {
  max-width: 400px;
  width: 100%;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(77, 76, 76, 0.1);

  border-radius: 8px;
  text-align: center;
  /* 去掉边框 */
  border: none;
  /* 透明 */
  background-color: rgba(255, 255, 255, 0.6);
  /* 模糊 */
  backdrop-filter: blur(2px);
}

.login-button {
  width: 160px;
  height: 40px;
  background-color: #3498db; /* 主题色调整为淡蓝色 */
  color: #fff; /* 文字颜色设置为白色 */
  border: none; /* 移除按钮边框 */
}
</style>
