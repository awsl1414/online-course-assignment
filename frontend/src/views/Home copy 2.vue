<template>
  <el-container class="layout-container-demo">
    <!-- 侧边栏 -->
    <el-aside width="200px">
      <el-scrollbar>
        <el-menu :default-openeds="['1']">
          <el-sub-menu index="1">
            <template #title> 机房查询 </template>
            <el-menu-item-group title="Group 1"> </el-menu-item-group>
            <el-sub-menu index="1-1">
              <template @click="getFloorHandle" #title>楼层</template>
              <el-menu-item @click="getOriginClassHandle" index="1-1-1"
                >C楼</el-menu-item
              >
            </el-sub-menu>
            <!-- <el-sub-menu
              v-for="(floor, index) in floorData"
              :key="index"
              :index="index"
            >
              {{ floor }}
            </el-sub-menu> -->
            <el-menu-item-group title="Group 2">
              <el-menu-item index="1-2">Option 2</el-menu-item>
            </el-menu-item-group>
            <el-sub-menu index="1-3">
              <template #title>Option3</template>
              <el-menu-item index="1-3-1">Option 3-1</el-menu-item>
            </el-sub-menu>
          </el-sub-menu>
          <!-- 其他菜单项 -->
        </el-menu>
      </el-scrollbar>
    </el-aside>

    <!-- 主体区域 -->
    <el-container>
      <!-- 头部 -->
      <el-header style="text-align: right; font-size: 12px">
        <div class="toolbar">
          <el-dropdown>
            <el-icon style="margin-right: 8px; margin-top: 1px"
              ><setting
            /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>View</el-dropdown-item>
                <el-dropdown-item>Add</el-dropdown-item>
                <el-dropdown-item>Delete</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 主体内容 -->
      <el-main>
        <el-scrollbar>
          <el-table :data="originClassData">
            <el-table-column prop="teacherName" label="教师" />
            <el-table-column prop="teacherRoom" label="教研室" />
            <el-table-column prop="className" label="班级" />
            <el-table-column prop="courseName" label="课程名" />
            <el-table-column prop="software" label="软件" />
          </el-table>
        </el-scrollbar>
      </el-main>
    </el-container>
  </el-container>
  <div><button @click="getFloorHandle">测试按钮</button></div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import axios from "../axios/index.js";

const ORIGIN_CLASS_URL = "/api/v1/get_origin_course";
const FLOOR_URL = "/api/v1/get_computer_room_floor";

const originClassData = ref();
const floorData = ref();

const testHandle = () => {
  console.log("");
};

const getOriginClassHandle = () => {
  axios.get(ORIGIN_CLASS_URL).then((res) => {
    console.log(res.data);
    originClassData.value = res.data;
  });
};

const getFloorHandle = () => {
  axios.get(FLOOR_URL).then((res) => {
    console.log(res.data);
    floorData.value = res.data;
  });
};
</script>

<style scoped>
.layout-container-demo {
  height: auto;
}

.layout-container-demo .el-header {
  position: relative;
  background-color: var(--el-color-primary-light-7);
  color: var(--el-text-color-primary);
}

.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}

.layout-container-demo .el-menu {
  border-right: none;
}

.layout-container-demo .el-main {
  padding: 0;
}

.layout-container-demo .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: flex-end;
  height: 100%;
  margin-right: 20px;
}
</style>
