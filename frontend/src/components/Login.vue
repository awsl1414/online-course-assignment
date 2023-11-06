<template>
  <div class="maxbox">
    <div class="box">
      <h1>welcome</h1>
      <div class="login-box">
        <form>
          <div class="input-box">
            用户：<input
              type="text"
              v-model="username"
              placeholder="账号"
            /><br />
          </div>

          <div class="input-box">
            密码：<input
              type="password"
              v-model="password"
              placeholder="密码"
            /><br />
          </div>

          <div>
            <el-button @click="login()" type="primary" plain>登录</el-button
            ><br />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { selectGroupKey } from "element-plus";
import { compile, computed, ref } from "vue";
import { ElButton } from "element-plus";

const count = ref(0);
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
    };
  },

  methods: {
    login() {
      let params = new URLSearchParams(); //应该是将params定义为对象吧
      params.append("username", this.username);
      params.append("password", this.password);
      axios
        .post(`http://49.235.107.169:5000/api/v1/login`, params, {
          headers: {
            Accept: "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
          },
        })
        .then((ret) => {
          if (ret.data.code != 200) {
            console.log(`账号或密码错误`);
            alert("账号或密码错误");
          } else {
            console.log(ret.data.code);
            console.log(ret.data.token);
            localStorage.setItem("token", ret.data.token);
            this.$router.push("/work");
            console.log(`试试${this.username},${this.password}`);
          }
        });
    },
  },
};
</script>

<style>
.maxbox {
  background: url("../image/Loginbackground.jpg") no-repeat;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  margin: 0px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-size: cover;
}
* {
  margin: 0;
  padding: 0;
}

body {
  width: 100%;
  height: 100%;
}

.box {
  border-radius: 20px;
  height: 380px;
  width: 350px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  top: 1px solid rgba(255, 255, 255, 0.5);
  left: 1px solid rgba(255, 255, 255, 0.5);
  bottom: 1px solid rgba(255, 255, 255, 0.5);
  right: 1px solid rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
  background: rgba(50, 50, 50, 0.2);
}

.box > h2 {
  color: rgba(255, 255, 255, 0.9);
}

.box .input-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}

.box .input-box > label {
  color: rgba(255, 255, 255, 0.9);
  font-size: 13px;
}

.box .input-box > input {
  box-sizing: border-box;
  color: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  height: 35px;
  width: 250px;
  background: rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 5px;
  transition: 0.2s;
  padding: 0 10px;
  letter-spacing: 1px;
}

.box .input-box > input:focus {
  border: 1px solid rgba(255, 255, 255, 0.8);
}
.box .btn-box {
  width: 250px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}

.box .btn-box > a {
  font-size: 14px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.9);
  transition: 0.2s;
  text-align: end;
  width: 250px;
}
.box .btn-box > a:hover {
  color: rgba(255, 255, 255, 1);
}

.box .btn-box > div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: start;
  margin-top: 20px;
}

.box .btn-box > div > button {
  width: 120px;
  height: 35px;
  border: 1px solid rgba(197, 81, 58, 0.8);
  background: rgba(197, 81, 58, 0.5);
  color: rgba(255, 255, 255, 0.9);
  border-radius: 5px;
}
.box .btn-box > div > button:hover {
  width: 120px;
  height: 35px;
  border: 1px solid rgba(197, 81, 58, 0.8);
  background: rgba(197, 81, 58, 0.5);
  color: rgba(255, 255, 255, 0.9);
  border-radius: 5px;
  transition: 0.2s;
}

.box .btn-box > div > button:nth-of-type(2) {
  margin-left: 10px;
}

.box .btn-box > div > button:hover {
  border: 1px solid rgba(248, 108, 76, 0.8);
  background: rgba(248, 108, 79, 0.5);
}
.btn-login {
  margin: 0 auto;
  position: relative;
}
.btn-enroll {
  margin: 0 auto;
  position: relative;
}
.btn-forget {
  margin: 0 auto;
  position: relative;
}
</style>
