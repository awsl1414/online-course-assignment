<template>
  <div class="row">
    <div class="col-2">
      <div class="form-group">
        <div
          class="btn-group-vertical buttons"
          role="group"
          aria-label="Basic example"
        >
          <button class="btn btn-secondary" @click="add">Add</button>
          <button class="btn btn-secondary" @click="replace">Replace</button>
        </div>

        <div class="form-check">
          <input
            id="disabled"
            type="checkbox"
            v-model="enabled"
            class="form-check-input"
          />
          <label class="form-check-label" for="disabled">DnD enabled</label>
        </div>
      </div>
    </div>

    <div class="col-6">
      <h3>Draggable {{ draggingInfo }}</h3>

      <draggable
        :list="list"
        :disabled="!enabled"
        item-key="name"
        class="list-group"
        ghost-class="ghost"
        :move="checkMove"
        @start="dragging = true"
        @end="dragging = false"
      >
        <template #item="{ element }">
          <div class="list-group-item" :class="{ 'not-draggable': !enabled }">
            <table title="hhh">
              <tr>
                <td>
                  {{ element.name }}
                </td>
                |
                <td>154141</td>
              </tr>
            </table>
          </div>
        </template>
      </draggable>
    </div>

    <rawDisplayer class="col-3" :value="list" title="List" />
  </div>
</template>

<script>
import draggable from "vuedraggable";
import { ref } from "vue";

export default {
  name: "simple",
  display: "Simple",
  order: 0,
  components: {
    draggable,
  },
  setup() {
    const enabled = ref(true);
    const list = ref([
      { name: "John", id: 0 },
      { name: "Joao", id: 1 },
      { name: "Jean", id: 2 },
    ]);
    const dragging = ref(false);

    const add = (id) => {
      list.value.push({ name: "Juan " + id.value, id: id.value++ });
    };

    const replace = (id) => {
      list.value = [{ name: "Edgard", id: id.value++ }];
    };

    const checkMove = (e) => {
      console.log("Future index: " + e.draggedContext.futureIndex);
    };

    return { enabled, list, dragging, add, replace, checkMove };
  },
  computed: {
    draggingInfo() {
      return this.dragging ? "under drag" : "";
    },
  },
};
</script>

<style scoped>
.buttons {
  margin-top: 35px;
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}

.not-draggable {
  cursor: no-drop;
}
</style>
