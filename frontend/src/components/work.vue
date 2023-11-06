<template>
  <div class="table">
    <el-table :data="tableData" style="width: 100%" height="250">
      <el-table-column fixed prop="room" label="机房" width="150" />
      <el-table-column prop="Monday" label="星期一" width="120" />
      <el-table-column prop="Tuesday" label="星期二" width="120" />
      <el-table-column prop="Wednesday" label="星期三" width="120" />
      <el-table-column prop="Thursday" label="星期四" width="120" /> -->
      <el-table-column prop="Friday" label="星期五" width="120" /> -->
      <el-table-column prop="Saturday" label="星期六" width="100" />
      <el-table-column prop="Sunday" label="星期日" width="120" /> -->
    </el-table>

    <el-dropdown>
      <el-button type="primary">
        选择楼层<el-icon class="el-icon--right"><arrow-down /></el-icon>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item v-for="p in floor" @click="selectRoom(p)">
            {{ p }}
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
</template>

<script setup>
import { ArrowDown } from "@element-plus/icons-vue";
import axios from "axios";
import { ref, onMounted } from "vue";

let floor = ref();
let room = ref();
let tableData = ref();

onMounted(() => {
  axios({
    methods: "get",
    url: `http://127.0.0.1:4523/m1/3490940-0-default/api/v1/computer_room/floor?computer_room_floor=B5`,
  }).then((res) => {
    if (res.data.code == 200) {
      floor.value = Object.keys(res.data.floor);
      room.value = res.data.floor;
      console.log(floor.value);
      console.log(room.value);
    } else {
      console.log("后端楼层返回错误");
    }
  });
});

const selectRoom = (selectedRoom) => {
  // 更新tableData，显示所选楼层的数据
  // room.value = room.value[selectedRoom];
  tableData.value = room.value[selectedRoom];
};
</script>

<style>
.table {
  margin: 0 auto;
  width: 80%;
  height: 80%;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 10px #999999;
  padding: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
