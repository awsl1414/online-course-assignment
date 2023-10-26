<template>
  <div class="course-table">
    <el-table :data="tableData" border>
      <el-table-column prop="classroom" label="时间/机房" width="150" />

      <el-table-column v-for="day in days" :key="day.en" :label="day.cn" colspan="3" align="center">
        <el-table-column label="上午" colspan="2" align="center">
          <el-table-column :prop="`${day.en}Morning1`" width="100" label="1-2节" align="center">
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
          <el-table-column :prop="`${day.en}Morning2`" width="100" label="3-4节" align="center">
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
        </el-table-column>
        <el-table-column label="下午" colspan="2" align="center">
          <el-table-column :prop="`${day.en}Afternoon1`" width="100" label="5-6节" align="center">
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
          <el-table-column :prop="`${day.en}Afternoon2`" width="100" label="7-8节" align="center">
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
        </el-table-column>
        <el-table-column label="晚上" width="120" align="center">
          <el-table-column :prop="`${day.en}Evening`" width="100" label="9-10节" align="center">
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
        </el-table-column>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const tableData = ref([
  {
    classroom: 'B501/机房01',
    mondayMorning1: 'B501周一上午1-2节',
    mondayMorning2: 'B501周一上午3-4节',
    mondayAfternoon1: '内容5-6',
    mondayAfternoon2: '内容7-8',
    mondayEvening: '内容9-10',
    tuesdayMorning1: '内容1-2',
    tuesdayMorning2: '内容3-4',
    tuesdayAfternoon1: '内容5-6',
    tuesdayAfternoon2: '内容7-8',
    tuesdayEvening: '内容9-10',
    wednesdayMorning1: '内容1-2',
  },
  {
    classroom: 'B502/机房02',
    mondayMorning1: '内容1-2',
    mondayMorning2: '内容3-4',
    mondayAfternoon1: '内容5-6',
    mondayAfternoon2: '内容7-8',
    mondayEvening: '内容9-10',
    tuesdayMorning1: '内容1-2',
    tuesdayMorning2: '内容3-4',
    tuesdayAfternoon1: '内容5-6',
    tuesdayAfternoon2: '内容7-8',
    tuesdayEvening: '内容9-10',
    wednesdayMorning1: '内容1-2',
  },
  {
    classroom: 'B503/机房03',
    mondayMorning1: 'B503周一上午1-2节',
    mondayMorning2: '内容3-4',
    mondayAfternoon1: '内容5-6',
    mondayAfternoon2: '内容7-8',
    mondayEvening: '内容9-10',
    tuesdayMorning1: '内容1-2',
    tuesdayMorning2: '内容3-4',
    tuesdayAfternoon1: '内容5-6',
    tuesdayAfternoon2: '内容7-8',
    tuesdayEvening: '内容9-10',
    wednesdayMorning1: '内容1-2',
  },
]);

const days = [
  { en: 'monday', cn: '星期一' },
  { en: 'tuesday', cn: '星期二' },
  { en: 'wednesday', cn: '星期三' },
  { en: 'thursday', cn: '星期四' },
  { en: 'friday', cn: '星期五' },
  { en: 'saturday', cn: '星期六' },
];

let draggedData = null;

const onDragStart = (event, row, prop) => {
  draggedData = { value: row[prop], row, prop };
  event.dataTransfer.setData('text/plain', ''); // for Firefox compatibility
};

const onDrop = (event, targetRow, targetProp) => {
  if (draggedData) {
    const targetValue = targetRow[targetProp];

    if (!targetValue || targetValue.trim() === "") {
      targetRow[targetProp] = draggedData.value;
      draggedData.row[draggedData.prop] = "";
    } else {
      targetRow[targetProp] = draggedData.value;
      draggedData.row[draggedData.prop] = targetValue;
    }

    draggedData = null;
  }
};
</script>

<style scoped>
.course-table {
  margin: 20px;
  border: 1px solid #ebebeb;
}
</style>
