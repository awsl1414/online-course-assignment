<template>
    <div class="container">
      <div class="title">欢迎登录</div>
      <input type="text" placeholder="用户名" v-model="username" />
      <input type="password" placeholder="密码" v-model="password" />
      <button @click="login">登录</button>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    setup() {
      const username = ref("");
      const password = ref("");
  
      const login = () => {
        if (username.value && password.value) {
          alert("登录成功");
        } else {
          alert("请填写用户名和密码");
        }
      };
  
      return {
        username,
        password,
        login,
      };
    },
  };
  </script>
  
  <style scoped>
  body {
    font-family: "Arial", sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f2f2f2;
  }
  
  .container {
    width: 300px;
    max-width: 90%;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 5px;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
  }
  
  .forgot-link {
    text-align: center;
    margin-top: 10px;
  }
  </style>
  