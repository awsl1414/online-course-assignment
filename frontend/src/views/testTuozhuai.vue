<template>
    <div class="course-table">
      <el-table :data="courses" border>
        <el-table-column prop="day" label="Day" width="120">
          <template v-slot:default="{ row, column }">
            <div
              :draggable="true"
              @dragstart="onDragStart($event, row, column.property)"
              @drop="onDrop($event, row, column.property)"
              @dragover.prevent
            >
              {{ row[column.property] || '\u00A0' }}
            </div>
          </template>
        </el-table-column>
        
        <el-table-column prop="time" label="Time" width="120">
          <template v-slot:default="{ row, column }">
            <div
              :draggable="true"
              @dragstart="onDragStart($event, row, column.property)"
              @drop="onDrop($event, row, column.property)"
              @dragover.prevent
            >
              {{ row[column.property] || '\u00A0' }}
            </div>
          </template>
        </el-table-column>
        
        <el-table-column prop="subject" label="Subject">
          <template v-slot:default="{ row, column }">
            <div
              :draggable="true"
              @dragstart="onDragStart($event, row, column.property)"
              @drop="onDrop($event, row, column.property)"
              @dragover.prevent
            >
              {{ row[column.property] || '\u00A0' }}
            </div>
          </template>
        </el-table-column>
        
        <el-table-column prop="teacher" label="Teacher">
          <template v-slot:default="{ row, column }">
            <div
              :draggable="true"
              @dragstart="onDragStart($event, row, column.property)"
              @drop="onDrop($event, row, column.property)"
              @dragover.prevent
            >
              {{ row[column.property] || '\u00A0' }}
            </div>
          </template>
        </el-table-column>
        
        <el-table-column prop="room" label="Room">
          <template v-slot:default="{ row, column }">
            <div
              :draggable="true"
              @dragstart="onDragStart($event, row, column.property)"
              @drop="onDrop($event, row, column.property)"
              @dragover.prevent
            >
              {{ row[column.property] || '\u00A0' }}
            </div>
          </template>
        </el-table-column>
  
      </el-table>
    </div>
  </template>
  
  
  <script setup>
  import { ref } from 'vue';
  
  const courses = ref([
    { day: 'Monday', time: '9:00-10:00', subject: 'Math', teacher: 'Mr. Smith', room: 'A101' },
    { day: 'Monday', time: '10:00-11:00', subject: '', teacher: '',room: 'A102' },
    // ... 其他的课程数据
  ]);
  
  let draggedItemIndex = null;
  
  let draggedData = null;
  
  const onDragStart = (event, row, prop) => {
    console.log('drag start');
    draggedData = { value: row[prop], row, prop };
    event.dataTransfer.setData('text/plain', ''); // for Firefox compatibility
  };
  
  const onDrop = (event, targetRow, targetProp) => {
    console.log('drop');
    if (draggedData) {
      const targetValue = targetRow[targetProp];
  
      // 如果目标单元格没有内容
      if (!targetValue || targetValue.trim() === "") {
        targetRow[targetProp] = draggedData.value; // 目标单元格内容为源单元格内容
        draggedData.row[draggedData.prop] = ""; // 源单元格内容消失
      } else {
        // 如果目标单元格有内容，那么执行互换操作
        targetRow[targetProp] = draggedData.value;
        draggedData.row[draggedData.prop] = targetValue;
      }
      
      draggedData = null;
    }
  };
  
  // const tableDrop = (event) => {
  //   event.preventDefault();
  // };
  </script>
  
  <style scoped>
  .course-table {
    margin: 20px;
    border: 1px solid #ebebeb;
  }
  </style>
  